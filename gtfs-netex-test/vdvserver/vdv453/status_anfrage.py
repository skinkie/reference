from dataclasses import dataclass
from .status_anfrage_type import StatusAnfrageType


@dataclass(kw_only=True)
class StatusAnfrage(StatusAnfrageType):
    pass
