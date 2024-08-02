from dataclasses import dataclass, field
from typing import Optional, Union

from .luggage_spot_ref import LuggageSpotRef
from .passenger_spot_ref import PassengerSpotRef
from .passenger_vehicle_spot_ref import PassengerVehicleSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocatableSpotRangeRefStructure:
    locatable_spot_ref: Optional[Union[LuggageSpotRef, PassengerVehicleSpotRef, PassengerSpotRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LuggageSpotRef",
                    "type": LuggageSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerVehicleSpotRef",
                    "type": PassengerVehicleSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpotRef",
                    "type": PassengerSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
