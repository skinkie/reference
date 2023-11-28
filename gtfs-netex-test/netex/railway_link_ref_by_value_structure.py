from dataclasses import dataclass, field
from netex.link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RailwayLinkRefByValueStructure(LinkRefByValueStructure):
    """
    Type for a reference to a RAILWAY LINK BY VALUE.

    :ivar name_of_point_ref_class: Class of POINT referenced by LINK.
    """
    name_of_point_ref_class: str = field(
        init=False,
        default="RailwayPoint",
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        }
    )
