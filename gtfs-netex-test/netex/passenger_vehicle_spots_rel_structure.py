from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .passenger_vehicle_spot import PassengerVehicleSpot
from .passenger_vehicle_spot_ref import PassengerVehicleSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerVehicleSpotsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerVehicleSpots_RelStructure"

    passenger_vehicle_spot_ref_or_passenger_vehicle_spot: List[Union[PassengerVehicleSpotRef, PassengerVehicleSpot]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerVehicleSpotRef",
                    "type": PassengerVehicleSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerVehicleSpot",
                    "type": PassengerVehicleSpot,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
