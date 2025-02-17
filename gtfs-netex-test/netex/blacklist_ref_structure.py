from dataclasses import dataclass

from .security_list_ref_structure import SecurityListRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BlacklistRefStructure(SecurityListRefStructure):
    pass
