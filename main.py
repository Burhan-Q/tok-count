import sys
from pathlib import Path

import tiktoken
import typer

DEFAULT_MODEL = "gpt-5"  # maps to o200k_base

app = typer.Typer()


@app.command()
def main(
    file: Path = typer.Argument(
        None, exists=True, dir_okay=False, help="File to count; reads stdin if omitted"
    ),
    model: str = typer.Option(DEFAULT_MODEL, "--model", "-m", help="Model to encode with"),
):
    """Count tokens in a file or piped text."""
    if file is not None:
        text = file.read_text("utf-8")
    elif sys.stdin.isatty():
        typer.echo("no input: pass a file path or pipe text to stdin", err=True)
        raise typer.Exit(2)
    else:
        text = sys.stdin.read()

    try:
        enc = tiktoken.encoding_for_model(model)
    except KeyError:
        typer.echo(f"unknown model: {model}", err=True)
        raise typer.Exit(2)

    print(len(enc.encode(text)))


if __name__ == "__main__":
    app()
