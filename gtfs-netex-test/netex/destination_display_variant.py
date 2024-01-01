from dataclasses import dataclass
from .destination_display_variant_version_structure import (
    DestinationDisplayVariantVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariant(DestinationDisplayVariantVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
