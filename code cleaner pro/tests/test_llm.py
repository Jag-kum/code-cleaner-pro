import pytest
from unittest.mock import patch
from code_cleaner_pro.core import LLMIntegration

def test_llm_refactor_success():
    """Test successful LLM refactoring"""
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "choices": [{"message": {"content": "refactored code"}}]
        }
        
        llm = LLMIntegration(api_key="test-key")
        result = llm.refactor_with_llm("original code", "prompt")
        assert result == "refactored code"

def test_llm_refactor_failure():
    """Test LLM API failure handling"""
    with patch('requests.post') as mock_post:
        mock_post.return_value.raise_for_status.side_effect = Exception("API error")
        
        llm = LLMIntegration(api_key="test-key")
        with pytest.raises(Exception, match="LLM API error"):
            llm.refactor_with_llm("original code", "prompt")

def test_llm_no_api_key():
    """Test LLM initialization without API key"""
    with pytest.raises(ValueError, match="API key is required"):
        LLMIntegration(api_key=None)

def test_llm_invalid_api_key():
    """Test LLM initialization with empty API key"""
    with pytest.raises(ValueError, match="API key is required"):
        LLMIntegration(api_key="")