from dataclasses import dataclass, field
from netex.destination_display_version_structure import DestinationDisplayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplay(DestinationDisplayVersionStructure):
    """
    An advertised destination of a specific JOURNEY PATTERN, usually displayed on a
    head sign or at other on-board locations.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
