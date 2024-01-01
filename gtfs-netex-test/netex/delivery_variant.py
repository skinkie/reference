from dataclasses import dataclass
from .delivery_variant_version_structure import DeliveryVariantVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeliveryVariant(DeliveryVariantVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
