from dataclasses import dataclass
from netex.price_unit_ref_structure import PriceUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PriceUnitRef(PriceUnitRefStructure):
    """
    Reference to a PRICE UNIT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
