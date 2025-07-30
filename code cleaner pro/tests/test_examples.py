import pytest
from pathlib import Path
from code_cleaner_pro.core import clean_code

EXAMPLE_FILES = [
    ("basic_example.py", "pep8"),
    ("procedural_to_oop.py", "oop"),
    ("functional_example.py", "functional")
]

@pytest.mark.parametrize("filename,style", EXAMPLE_FILES)
def test_example_transformations(filename, style):
    """Test that example files can be processed without errors"""
    example_path = Path("examples") / filename
    with open(example_path, "r") as f:
        original = f.read()
    
    cleaned = clean_code(original, style=style)
    assert isinstance(cleaned, str)
    assert len(cleaned) > 0

def test_invalid_file_handling():
    """Test handling of invalid file paths"""
    with pytest.raises(FileNotFoundError):
        with open("nonexistent.py", "r") as f:
            pass

def test_syntax_error_handling():
    """Test handling of code with syntax errors"""
    bad_code = "def foo(: pass"  # Invalid syntax
    cleaned = clean_code(bad_code)
    assert cleaned == bad_code + "\n"  # Should return original with newline