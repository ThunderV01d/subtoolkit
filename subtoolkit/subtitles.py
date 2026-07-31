from pathlib import Path
import pysubs2
from .models import SubtitleEntry

def load(path: Path) -> list[SubtitleEntry]:
    """Load an SRT file."""

    subs = pysubs2.load(str(path))

    entries = []

    for line in subs:
        entries.append(
            SubtitleEntry(
                start_ms=line.start,
                end_ms=line.end,
                text=line.text,
            )
        )

    return entries

def save(
    subtitles: list[SubtitleEntry],
    path: Path,
):
    """Write subtitles to disk."""

    subs = pysubs2.SSAFile()

    for subtitle in subtitles:
        subs.append(
            pysubs2.SSAEvent(
                start=subtitle.start_ms,
                end=subtitle.end_ms,
                text=subtitle.text,
            )
        )

    subs.save(str(path))