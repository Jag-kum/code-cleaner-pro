import pytest
from unittest.mock import Mock, patch
from code_cleaner_pro.core import clean_code

@pytest.fixture
def mock_llm():
    with patch('code_cleaner_pro.core.LLMIntegration') as mock:
        mock.return_value.refactor_with_llm.return_value = "cleaned code"
        yield mock

@pytest.fixture
def sample_code():
    return "def foo(): pass"

@pytest.fixture
def tmp_code_file(tmp_path):
    file = tmp_path / "test.py"
    file.write_text("def foo(): pass")
    return file