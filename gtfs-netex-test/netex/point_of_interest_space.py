from dataclasses import dataclass, field
from netex.point_of_interest_space_version_structure import PointOfInterestSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestSpace(PointOfInterestSpaceVersionStructure):
    """
    A PLACE within a POINT OF INTEREST.

    :ivar id: Identifier of POINT OF INTEREST SPACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
