from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.point_of_interest_entrance import PointOfInterestEntrance
from netex.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestEntrancesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of POINT OF INTEREST ENTRANCEs.
    """
    class Meta:
        name = "pointOfInterestEntrances_RelStructure"

    point_of_interest_entrance_ref_or_point_of_interest_entrance: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOfInterestEntranceRef",
                    "type": SiteComponentRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntrance",
                    "type": PointOfInterestEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
