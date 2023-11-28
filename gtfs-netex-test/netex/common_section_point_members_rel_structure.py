from dataclasses import dataclass, field
from typing import List
from netex.common_section_point_member import CommonSectionPointMember
from netex.line_section_point_member import LineSectionPointMember
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommonSectionPointMembersRelStructure(StrictContainmentAggregationStructure):
    """DEPRECATED - Type for a list of COMMON SECTION POINT MEMBERs."""
    class Meta:
        name = "commonSectionPointMembers_RelStructure"

    line_section_point_member_or_common_section_point_member: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LineSectionPointMember",
                    "type": LineSectionPointMember,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSectionPointMember",
                    "type": CommonSectionPointMember,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
