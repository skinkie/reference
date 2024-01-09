from dataclasses import dataclass
from .abo_antwort_type import AboAntwortType


@dataclass(kw_only=True)
class AboAntwort(AboAntwortType):
    pass
