from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .individual_passenger_info import IndividualPassengerInfo

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class IndividualPassengerInfosRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "individualPassengerInfos_RelStructure"

    individual_passenger_info: list[IndividualPassengerInfo] = field(
        default_factory=list,
        metadata={
            "name": "IndividualPassengerInfo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
