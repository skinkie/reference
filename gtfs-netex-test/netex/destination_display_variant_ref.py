from dataclasses import dataclass
from netex.destination_display_variant_ref_structure import DestinationDisplayVariantRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayVariantRef(DestinationDisplayVariantRefStructure):
    """
    Reference to a DESTINATION DISPLAY VARIANT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
