"""Code Cleaner Pro - A tool to clean and reformat code according to style guides."""
from .core import (
    clean_code,
    LLMIntegration,
    remove_trailing_whitespace,
    normalize_line_endings,
    ensure_final_newline,
    SUPPORTED_STYLES
)

__version__ = "0.2.0"