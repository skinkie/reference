from dataclasses import dataclass
from netex.security_list_ref_structure import SecurityListRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WhitelistRefStructure(SecurityListRefStructure):
    """
    Type for Reference to a WHITELIST.
    """
