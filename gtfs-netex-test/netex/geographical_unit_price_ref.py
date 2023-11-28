from dataclasses import dataclass
from netex.geographical_unit_price_ref_structure import GeographicalUnitPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnitPriceRef(GeographicalUnitPriceRefStructure):
    """
    Reference to a GEOGRAPHICAL UNIT PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
