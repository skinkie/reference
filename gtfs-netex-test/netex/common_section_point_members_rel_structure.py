from dataclasses import dataclass, field
from typing import Union

from .common_section_point_member import CommonSectionPointMember
from .line_section_point_member import LineSectionPointMember
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CommonSectionPointMembersRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "commonSectionPointMembers_RelStructure"

    common_section_point_member: list[Union[LineSectionPointMember, CommonSectionPointMember]] = field(
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
        },
    )
