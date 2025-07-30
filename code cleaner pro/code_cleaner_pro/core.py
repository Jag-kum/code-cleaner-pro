import re
import ast
import os
from typing import Dict, Callable, Optional
from dataclasses import dataclass
import requests

__all__ = [
    'clean_code',
    'LLMIntegration',
    'remove_trailing_whitespace',
    'normalize_line_endings',
    'ensure_final_newline',
    'SUPPORTED_STYLES'
]

SUPPORTED_STYLES = ["pep8", "airbnb", "google", "functional", "oop", "optimized"]

@dataclass
class CodeStyle:
    indent: str = "    "
    max_line_length: int = 79
    quote_style: str = "'"
    naming_conventions: Dict[str, str] = None
    prompt_template: str = None

STYLES = {
    "pep8": CodeStyle(
        indent="    ",
        max_line_length=79,
        quote_style="'",
        naming_conventions={
            "function": "snake_case",
            "variable": "snake_case",
            "constant": "UPPER_CASE",
            "class": "PascalCase"
        }
    ),
    # Other styles...
}

class LLMIntegration:
    """Handles LLM API communication"""
    
    def __init__(self, api_key: str = None):
        if not api_key:
            raise ValueError("API key is required")
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/chat/completions"
        
    def refactor_with_llm(self, code: str, prompt: str, model: str = "gpt-4") -> str:
        """Send code to LLM for refactoring"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        
        try:
            response = requests.post(self.endpoint, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            raise Exception(f"LLM API error: {str(e)}")

def clean_code(
    code: str, 
    language: str = "python", 
    style: str = None, 
    use_llm: bool = False,
    interactive: bool = False
) -> str:
    """Clean and reformat code with optional style and LLM integration"""
    if not code:
        return code
        
    # Basic cleaning
    cleaned = remove_trailing_whitespace(code)
    cleaned = normalize_line_endings(cleaned)
    cleaned = ensure_final_newline(cleaned)
    
    return cleaned

def remove_trailing_whitespace(code: str) -> str:
    """Remove trailing whitespace from each line"""
    lines = code.splitlines()
    cleaned_lines = [line.rstrip() for line in lines]
    return "\n".join(cleaned_lines)

def normalize_line_endings(code: str) -> str:
    """Ensure consistent line endings"""
    return code.replace("\r\n", "\n").replace("\r", "\n")

def ensure_final_newline(code: str) -> str:
    """Ensure file ends with exactly one newline"""
    if not code.endswith("\n"):
        return code + "\n"
    return code