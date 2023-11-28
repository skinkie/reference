from dataclasses import dataclass
from netex.priceable_object_ref_structure import PriceableObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PriceableObjectRef(PriceableObjectRefStructure):
    """
    Reference to a PRICEABLE ELEMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
