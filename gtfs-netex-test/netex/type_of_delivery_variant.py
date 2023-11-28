from dataclasses import dataclass, field
from netex.type_of_delivery_variant_value_structure import TypeOfDeliveryVariantValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfDeliveryVariant(TypeOfDeliveryVariantValueStructure):
    """
    A classification of DELIVERY VARIANT according to its functional purpose.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
