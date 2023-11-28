from dataclasses import dataclass
from netex.all_operators_ref_structure import AllOperatorsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllOperatorsRef(AllOperatorsRefStructure):
    """
    Reference to all OPERATORs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
