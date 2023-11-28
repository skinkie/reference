from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.coupled_journey_ref import CoupledJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CoupledJourneysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of COUPLED JOURNEYS.
    """
    class Meta:
        name = "coupledJourneys_RelStructure"

    coupled_journey_ref: List[CoupledJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
