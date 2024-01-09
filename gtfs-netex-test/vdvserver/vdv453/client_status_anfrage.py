from dataclasses import dataclass
from .client_status_anfrage_type import ClientStatusAnfrageType


@dataclass(kw_only=True)
class ClientStatusAnfrage(ClientStatusAnfrageType):
    pass
