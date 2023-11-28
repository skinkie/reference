from dataclasses import dataclass
from netex.destination_display_derived_view_structure import DestinationDisplayDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayView(DestinationDisplayDerivedViewStructure):
    """Simplified view of a DESTINATION DISPLAY.

    Includes derived properties of the DESTINATION DISPLAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
