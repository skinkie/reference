from dataclasses import dataclass
from .abo_anfrage_type import AboAnfrageType


@dataclass(kw_only=True)
class AboAnfrage(AboAnfrageType):
    pass
