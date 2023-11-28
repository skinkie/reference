from dataclasses import dataclass
from netex.all_authorities_ref_structure import AllAuthoritiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllOperatorsRefStructure(AllAuthoritiesRefStructure):
    """
    Type for a reference to  all OPERATORss.
    """
