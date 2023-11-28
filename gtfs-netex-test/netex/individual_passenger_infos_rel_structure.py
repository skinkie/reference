from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.individual_passenger_info import IndividualPassengerInfo

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualPassengerInfosRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of INDIVIDUAL PASSENGER INFOs.
    """
    class Meta:
        name = "individualPassengerInfos_RelStructure"

    individual_passenger_info: List[IndividualPassengerInfo] = field(
        default_factory=list,
        metadata={
            "name": "IndividualPassengerInfo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
