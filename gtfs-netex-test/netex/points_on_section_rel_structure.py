from dataclasses import dataclass, field
from typing import List
from netex.point_on_line_section import PointOnLineSection
from netex.point_on_section import PointOnSection
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointsOnSectionRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of  POINTS on SECTION POINT   +v1.1.
    """
    class Meta:
        name = "pointsOnSection_RelStructure"

    point_on_line_section_or_point_on_section: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOnLineSection",
                    "type": PointOnLineSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOnSection",
                    "type": PointOnSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
