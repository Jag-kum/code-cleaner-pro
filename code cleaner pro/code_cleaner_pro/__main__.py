import typer
import pyperclip
import os
from pathlib import Path
from typing import Optional
from .core import clean_code, SUPPORTED_STYLES

app = typer.Typer(help="Code Cleaner Pro - Clean and reformat code according to style guides")

@app.command()
def main(
    source: Optional[str] = typer.Argument(None, help="File path or '-' for stdin"),
    style: str = typer.Option(
        None, 
        "--style", 
        help=f"Style to apply ({', '.join(SUPPORTED_STYLES)})",
        case_sensitive=False
    ),
    diff: bool = typer.Option(False, "--diff", help="Show diff between original and cleaned code"),
    write: bool = typer.Option(False, "--write", help="Overwrite source file with cleaned code"),
    clipboard: bool = typer.Option(False, "--clipboard", "-c", help="Copy output to clipboard"),
    llm: bool = typer.Option(False, "--llm", help="Use LLM for advanced refactoring"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Interactive mode for accepting changes"),
    model: str = typer.Option("gpt-4", "--model", help="LLM model to use (when --llm is enabled)")
):
    """
    Clean and reformat code from a file, stdin, or clipboard.
    """
    # Get input
    if source == "-":
        code = sys.stdin.read()
    elif source is None:
        code = pyperclip.paste()
    else:
        with open(source, "r") as f:
            code = f.read()

    # Clean the code
    cleaned = clean_code(
        code, 
        style=style,
        use_llm=llm,
        interactive=interactive
    )

    # Handle output
    if diff:
        show_diff(code, cleaned)
    if write and source and source != "-":
        with open(source, "w") as f:
            f.write(cleaned)
    if clipboard:
        pyperclip.copy(cleaned)
    if not (diff or write or clipboard):
        print(cleaned)

def show_diff(original: str, cleaned: str):
    """Display a side-by-side diff of changes"""
    from rich.console import Console
    from rich.syntax import Syntax
    from rich.text import Text
    
    console = Console()
    console.print(Text("Original", style="bold red"))
    console.print(Syntax(original, "python"))
    console.print(Text("\nCleaned", style="bold green"))
    console.print(Syntax(cleaned, "python"))

if __name__ == "__main__":
    app()