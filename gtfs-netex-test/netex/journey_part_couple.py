from dataclasses import dataclass, field
from netex.journey_part_couple_version_structure import JourneyPartCoupleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartCouple(JourneyPartCoupleVersionStructure):
    """
    Two or more  JOURNEY PARTs of different VEHICLE JOURNEYs served simultaneously
    by a train set up by coupling their single vehicles.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
