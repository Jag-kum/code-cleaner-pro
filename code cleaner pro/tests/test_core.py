import pytest
from code_cleaner_pro.core import (
    clean_code,
    remove_trailing_whitespace,
    normalize_line_endings,
    ensure_final_newline
)

def test_remove_trailing_whitespace():
    """Test whitespace removal from line ends"""
    code = "def foo():\n    pass    \n\n"
    expected = "def foo():\n    pass\n\n"
    assert remove_trailing_whitespace(code) == expected

def test_normalize_line_endings():
    """Test line ending normalization"""
    code = "def foo():\r\n    pass\r"
    expected = "def foo():\n    pass\n"
    assert normalize_line_endings(code) == expected

def test_ensure_final_newline():
    """Test final newline enforcement"""
    code = "def foo():\n    pass"
    expected = "def foo():\n    pass\n"
    assert ensure_final_newline(code) == expected

@pytest.mark.parametrize("style", ["pep8", "functional", "oop", "optimized"])
def test_clean_code_styles(style, monkeypatch):
    """Test all style modes work without LLM"""
    code = "def foo(): pass"
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    result = clean_code(code, style=style)
    assert isinstance(result, str)

def test_llm_integration(monkeypatch):
    """Test LLM integration error handling"""
    code = "def foo(): pass"
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    with pytest.raises(Exception):
        clean_code(code, style="functional", use_llm=True)

def test_empty_code():
    """Test handling empty input"""
    assert clean_code("") == ""

def test_none_code():
    """Test handling None input"""
    assert clean_code(None) is None