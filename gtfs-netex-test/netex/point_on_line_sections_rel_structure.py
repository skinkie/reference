from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.point_on_line_section import PointOnLineSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnLineSectionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of POINTS ON LINE SECTIONs.
    """
    class Meta:
        name = "pointOnLineSections_RelStructure"

    point_on_line_section: List[PointOnLineSection] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLineSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
