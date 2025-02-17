from dataclasses import dataclass

from .connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ConnectionRef(ConnectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
