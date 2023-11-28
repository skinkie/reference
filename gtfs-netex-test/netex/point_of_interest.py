from dataclasses import dataclass, field
from netex.point_of_interest_version_structure import PointOfInterestVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterest(PointOfInterestVersionStructure):
    """
    A type of SITE to or through which passengers may wish to navigate as part of
    their journey and which is modelled in detail by journey planners.

    :ivar id: Identifier of POINT OF INTEREST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
