from dataclasses import dataclass, field
from netex.delivery_variant_version_structure import DeliveryVariantVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeliveryVariant(DeliveryVariantVersionStructure):
    """
    A variant text of a NOTICE for use in a specific media or delivery channel
    (voice, printed material, etc).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
