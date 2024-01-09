from dataclasses import dataclass
from .status_antwort_type import StatusAntwortType


@dataclass(kw_only=True)
class StatusAntwort(StatusAntwortType):
    pass
