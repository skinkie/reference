from dataclasses import dataclass
from .connection_end_structure import ConnectionEndStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionEnd(ConnectionEndStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
