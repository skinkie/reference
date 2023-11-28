from dataclasses import dataclass, field
from netex.overtaking_possibility_version_structure import OvertakingPossibilityVersionStructure
from netex.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OvertakingPossibility(OvertakingPossibilityVersionStructure):
    """
    NETWORK RESTRICTION specifying a POINT or a LINK where vehicles of specified
    VEHICLE TYPEs are or are  not allowed to overtake each other.

    :ivar overtaking_at_point_ref: Identifier of a point at which two
        vehicles of the specified VEHICLE TYPE may pass.
    :ivar id:
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    overtaking_at_point_ref: PointRefStructure = field(
        metadata={
            "name": "OvertakingAtPointRef",
            "type": "Element",
            "required": True,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
