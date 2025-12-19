from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class WordEntry:
    word: str
    definition: Optional[str] = None
    date: Optional[date] = None