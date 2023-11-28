from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.delivery_variant_type_enumeration import DeliveryVariantTypeEnumeration
from netex.multilingual_string import MultilingualString
from netex.type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeliveryVariantVersionStructure(DataManagedObjectStructure):
    """
    Type for DELIVERY VARIANT.

    :ivar parent_ref: Parent of  DELIVERY VARIANT.
    :ivar delivery_variant_media_type: Type of DELIVERY VARIANT.
    :ivar type_of_delivery_variant_ref:
    :ivar variant_text: NOTICE variant  text.
    :ivar order: Presentation Order of variant.
    """
    class Meta:
        name = "DeliveryVariant_VersionStructure"

    parent_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delivery_variant_media_type: Optional[DeliveryVariantTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeliveryVariantMediaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_delivery_variant_ref: Optional[TypeOfDeliveryVariantRef] = field(
        default=None,
        metadata={
            "name": "TypeOfDeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    variant_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "VariantText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
