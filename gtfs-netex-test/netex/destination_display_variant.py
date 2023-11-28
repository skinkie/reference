from dataclasses import dataclass, field
from netex.destination_display_variant_version_structure import DestinationDisplayVariantVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayVariant(DestinationDisplayVariantVersionStructure):
    """
    A variant text of a DESTINATION DISPLAY for informational purposes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
