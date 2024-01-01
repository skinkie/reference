from dataclasses import dataclass
from .point_on_line_section_versioned_child_structure import (
    PointOnLineSectionVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineSectionPointMember(PointOnLineSectionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
