from dataclasses import dataclass
from .daten_bereit_anfrage_type import DatenBereitAnfrageType


@dataclass(kw_only=True)
class DatenBereitAnfrage(DatenBereitAnfrageType):
    pass
