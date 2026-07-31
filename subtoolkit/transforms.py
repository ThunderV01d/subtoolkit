from .models import SubtitleEntry


def apply_offset(
    subtitles: list[SubtitleEntry],
    offset_ms: int,
) -> list[SubtitleEntry]:

    shifted = []

    for subtitle in subtitles:

        shifted.append(
            SubtitleEntry(
                start_ms=max(0, subtitle.start_ms + offset_ms),
                end_ms=max(0, subtitle.end_ms + offset_ms),
                text=subtitle.text,
            )
        )

    return shifted