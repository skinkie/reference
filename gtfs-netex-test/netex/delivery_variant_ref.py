from dataclasses import dataclass
from netex.delivery_variant_ref_structure import DeliveryVariantRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeliveryVariantRef(DeliveryVariantRefStructure):
    """
    Reference to a DELIVERY VARIANT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
