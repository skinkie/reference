from dataclasses import dataclass, field
from typing import Optional
from netex.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnLinkRefStructure2(PointRefStructure):
    """
    Type for a reference to a POINT ON LINK.

    :ivar order: Order of point on link.
    """
    class Meta:
        name = "PointOnLinkRefStructure_"

    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
