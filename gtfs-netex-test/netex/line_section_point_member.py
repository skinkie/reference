from dataclasses import dataclass
from netex.point_on_line_section_versioned_child_structure import PointOnLineSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineSectionPointMember(PointOnLineSectionVersionedChildStructure):
    """
    [DEPRECATED use POINT ON LINE SECTION INSTEAD ] An ordered set of LINKs for a
    line.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
