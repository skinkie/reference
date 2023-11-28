from dataclasses import dataclass, field
from netex.point_of_interest_entrance_version_structure import PointOfInterestEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestEntrance(PointOfInterestEntranceVersionStructure):
    """
    Specialisation of ENTRANCE of ENTRANCE for a passenger to a POINT OF INTEREST.

    :ivar id: Identifier of POINT OF INTEREST ENTRANCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
