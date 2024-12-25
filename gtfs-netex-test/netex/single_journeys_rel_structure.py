from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .single_journey import SingleJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "singleJourneys_RelStructure"

    single_journey: list[SingleJourney] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
