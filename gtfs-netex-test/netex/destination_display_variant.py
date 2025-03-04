from dataclasses import dataclass

from .destination_display_variant_version_structure import DestinationDisplayVariantVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DestinationDisplayVariant(DestinationDisplayVariantVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
