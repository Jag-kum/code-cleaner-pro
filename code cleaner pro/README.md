# Code Cleaner Pro 🧹✨

A powerful Python command-line tool that automatically cleans, refactors, and transforms code according to various style guides and paradigms, with optional AI-powered transformations.

## Features

### Core Functionality
- **Multi-language support**: Works with Python, JavaScript, C++, and Java (Python fully implemented)
- **Multiple input sources**: Accepts code from files, stdin, or clipboard
- **Flexible output**: Output to terminal, files, or clipboard
- **Visual diffs**: Side-by-side comparison of changes
- **Interactive mode**: Approve/reject changes one-by-one

### Refactoring Modes
- **Standard styles**: PEP8 (Python), Airbnb (JavaScript), Google (C++)
- **Paradigm shifts**:
  - Functional programming conversion (map/filter/lambda)
  - Object-oriented transformation
  - Performance optimization
- **AI-powered refactoring**: Leverage LLMs for complex transformations

### Developer Experience
- **Modular architecture**: Easy to extend with new languages/styles
- **Comprehensive tests**: 90%+ test coverage
- **CI/CD ready**: GitHub Actions workflow included
- **Production-grade**: Proper error handling and logging

## Example Usage

```bash
# Basic cleaning
code-clean messy.py --style pep8 --diff

# AI-powered OOP conversion
code-clean procedural.py --style oop --llm

# Interactive functional transformation
code-clean loops.py --style functional --interactive

# Performance optimization
code-clean slow.py --style optimized --llm
```

## Installation

```bash
# Install normally
pip install .

# For development
pip install -e .[dev]
```

## Architecture

```
code_cleaner_pro/
├── __init__.py         # Package metadata
├── __main__.py         # CLI interface (Typer)
├── core.py             # Core cleaning logic
├── styles/             # Style configurations
├── transformers/       # Language-specific transformers
└── llm/                # AI integration

tests/                  # Comprehensive test suite
examples/               # Before/after examples
```

## Roadmap
- [ ] Add more language support
- [ ] Implement additional style guides
- [ ] Add VSCode extension
- [ ] Develop pre-commit hook

## Contributing
PRs welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License
MIT