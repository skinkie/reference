from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.single_journey import SingleJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a SINGLE JOURNEY.
    """
    class Meta:
        name = "singleJourneys_RelStructure"

    single_journey: List[SingleJourney] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
