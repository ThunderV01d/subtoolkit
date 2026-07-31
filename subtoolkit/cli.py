from pathlib import Path
from .subtitles import load, save
from .transforms import apply_offset

import typer

app = typer.Typer(
    help="AI-powered subtitle synchronization toolkit"
)

@app.command()
def sync(
    video:Path,
    subtitle:Path,
    offset_ms:int = typer.Option(0, "--offset","-o",help="Offset in milliseconds."),
    output:Path | None = typer.Option(None, "--output","-O",help="Output path for the synchronized subtitle file."),
    ):

    print(f"Video: {video}")
    print(f"Subtitle: {subtitle}")
    print(f"Offset: {offset_ms}")
    print(f"Output: {output}")

    entries = load(subtitle)
    entries = apply_offset(
        entries,
        int(offset_ms),
    )

    if output is None:
        output = subtitle.with_stem(f"{subtitle.stem}_synced")

    save(entries, output)

    print(f"Saved synchronized subtitle to {output}")

@app.command()
def version():
    print("0.1.0")

if __name__ == "__main__":
    app()