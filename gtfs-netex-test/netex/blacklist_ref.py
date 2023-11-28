from dataclasses import dataclass
from netex.blacklist_ref_structure import BlacklistRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlacklistRef(BlacklistRefStructure):
    """
    Reference to a BLACKLIST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
