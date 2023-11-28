from dataclasses import dataclass
from netex.point_on_section_versioned_child_structure import PointOnSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommonSectionPointMember(PointOnSectionVersionedChildStructure):
    """DEPRECATED - Kept for backwards compatibility POINT  Member of a COMMON SECTION.]"""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
