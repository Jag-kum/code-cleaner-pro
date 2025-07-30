import pytest
from typer.testing import CliRunner
from code_cleaner_pro.__main__ import app

runner = CliRunner()

def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Clean and reformat code" in result.output

def test_cli_file_input(tmp_code_file):
    result = runner.invoke(app, [str(tmp_code_file), "--style", "pep8"])
    assert result.exit_code == 0
    assert "def foo(): pass" in result.output

def test_cli_diff_flag(tmp_code_file):
    result = runner.invoke(app, [str(tmp_code_file), "--diff"])
    assert result.exit_code == 0
    assert "Original" in result.output
    assert "Cleaned" in result.output

def test_cli_invalid_style(tmp_code_file):
    result = runner.invoke(app, [str(tmp_code_file), "--style", "invalid"])
    assert result.exit_code != 0
    assert "Invalid style" in result.output

def test_cli_llm_flag(tmp_code_file, monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    result = runner.invoke(app, [str(tmp_code_file), "--llm"])
    assert result.exit_code == 0