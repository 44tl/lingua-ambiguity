import json

import typer

from .detectors import detect_all

app = typer.Typer()


@app.command()
def analyze(
    text: str = typer.Argument(..., help="Sentence to analyze for ambiguity.")
):
    ambiguities = detect_all(text)
    output = [a.model_dump() for a in ambiguities]
    typer.echo(json.dumps(output, indent=2))


if __name__ == "__main__":
    app()
