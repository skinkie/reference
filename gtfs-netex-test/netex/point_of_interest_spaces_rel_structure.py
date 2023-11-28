from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.point_of_interest_space import PointOfInterestSpace
from netex.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestSpacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of POINT OF INTEREST SPACEs.
    """
    class Meta:
        name = "pointOfInterestSpaces_RelStructure"

    point_of_interest_space_ref_or_point_of_interest_space: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": SiteComponentRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpace",
                    "type": PointOfInterestSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
