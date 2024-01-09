from dataclasses import dataclass
from .client_status_antwort_type import ClientStatusAntwortType


@dataclass(kw_only=True)
class ClientStatusAntwort(ClientStatusAntwortType):
    pass
