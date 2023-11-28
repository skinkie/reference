from dataclasses import dataclass
from netex.point_on_link_ref_structure_2 import PointOnLinkRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnLinkRefStructure1(PointOnLinkRefStructure2):
    """
    Type for a reference to a POINT ON LINK.
    """
    class Meta:
        name = "PointOnLinkRefStructure"
