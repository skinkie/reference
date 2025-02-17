from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .coupled_journey_ref import CoupledJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CoupledJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coupledJourneys_RelStructure"

    coupled_journey_ref: list[CoupledJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "CoupledJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
