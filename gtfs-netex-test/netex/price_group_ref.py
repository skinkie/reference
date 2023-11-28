from dataclasses import dataclass
from netex.price_group_ref_structure import PriceGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PriceGroupRef(PriceGroupRefStructure):
    """
    Reference to a PRICE GROUP.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
