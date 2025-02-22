from dataclasses import dataclass

from .delivery_variant_version_structure import DeliveryVariantVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeliveryVariant(DeliveryVariantVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
