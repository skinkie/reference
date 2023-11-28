from dataclasses import dataclass, field
from netex.journey_part_version_structure import JourneyPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPart(JourneyPartVersionStructure):
    """
    A part of a VEHICLE JOURNEY created according to a specific functional purpose,
    for instance in situations when vehicle coupling or separating occurs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
