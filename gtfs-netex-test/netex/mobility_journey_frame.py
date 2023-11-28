from dataclasses import dataclass, field
from netex.mobility_journey_version_frame_structure import MobilityJourneyVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityJourneyFrame(MobilityJourneyVersionFrameStructure):
    """
    A coherent set of MOBILITY JOURNEY data to which the same frame VALIDITY
    CONDITIONs have been assigned.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
