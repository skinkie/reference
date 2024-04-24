from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .passenger_spot import PassengerSpot
from .passenger_spot_ref import PassengerSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpotsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerSpots_RelStructure"

    passenger_spot_ref_or_passenger_spot: List[Union[PassengerSpotRef, PassengerSpot]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerSpotRef",
                    "type": PassengerSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpot",
                    "type": PassengerSpot,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
