from dataclasses import dataclass, field
from netex.journey_headway_versioned_child_structure import JourneyHeadwayVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyHeadway(JourneyHeadwayVersionedChildStructure):
    """Headway interval information that is available for all the VEHICLE JOURNEYs
    running on the JOURNEY PATTERN  for a given TIME DEMAND TYPE,  at a given
    TIMING POINT.

    This is a default value that can be superseded by VEHICLE JOURNEY
    HEADWAY. This information must be consistent with HEADWAY JOURNEY
    GROUP if available (HEADWAY JOURNEY GROUP being a more detailed way
    of describing headway services).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
