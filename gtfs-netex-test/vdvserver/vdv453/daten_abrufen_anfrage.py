from dataclasses import dataclass
from .daten_abrufen_anfrage_type import DatenAbrufenAnfrageType


@dataclass(kw_only=True)
class DatenAbrufenAnfrage(DatenAbrufenAnfrageType):
    pass
