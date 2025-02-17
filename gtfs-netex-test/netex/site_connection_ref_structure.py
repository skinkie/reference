from dataclasses import dataclass

from .connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteConnectionRefStructure(ConnectionRefStructure):
    pass
