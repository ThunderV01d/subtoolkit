from pathlib import Path
import typer

app = typer.Typer(
    help="AI-powered subtitle synchronization toolkit"
)

@app.command()
def sync(
    video:Path,
    subtitle:Path,
    offset:float = typer.Option(0.0, "--offset","-o",help="Number of milliseconds to offset the subtitle file. Positive values will push the subtitles forward, while negative values will bring them back."),
    output:Path | None = typer.Option(None, "--output","-O",help="Output path for the synchronized subtitle file."),
    ):

    print(f"Video: {video}")
    print(f"Subtitle: {subtitle}")
    print(f"Offset: {offset}")
    print(f"Output: {output}")

@app.command()
def version():
    print("0.1.0")

if __name__ == "__main__":
    app()