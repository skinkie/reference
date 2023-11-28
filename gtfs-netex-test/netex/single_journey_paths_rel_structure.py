from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.single_journey_path import SingleJourneyPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyPathsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a SINGLE JOURNEY PATH.
    """
    class Meta:
        name = "singleJourneyPaths_RelStructure"

    single_journey_path: List[SingleJourneyPath] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourneyPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
