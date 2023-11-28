from dataclasses import dataclass
from netex.whitelist_ref_structure import WhitelistRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WhitelistRef(WhitelistRefStructure):
    """
    Reference to a WHITELIST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
