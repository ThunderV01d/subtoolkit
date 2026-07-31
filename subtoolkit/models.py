from dataclasses import dataclass

@dataclass(slots=True)
class SubtitleEntry:
    start_ms: int
    end_ms: int
    text: str