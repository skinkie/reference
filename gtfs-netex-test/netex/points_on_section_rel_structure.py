from dataclasses import dataclass, field
from typing import Union

from .point_on_line_section import PointOnLineSection
from .point_on_section import PointOnSection
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointsOnSectionRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pointsOnSection_RelStructure"

    point_on_section: list[Union[PointOnLineSection, PointOnSection]] = field(
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
        },
    )
