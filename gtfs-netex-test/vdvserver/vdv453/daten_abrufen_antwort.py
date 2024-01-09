from dataclasses import dataclass
from .daten_abrufen_antwort_type import DatenAbrufenAntwortType


@dataclass(kw_only=True)
class DatenAbrufenAntwort(DatenAbrufenAntwortType):
    pass
