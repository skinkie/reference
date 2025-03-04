from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_on_line_section import PointOnLineSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOnLineSectionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointOnLineSections_RelStructure"

    point_on_line_section: list[PointOnLineSection] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLineSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
