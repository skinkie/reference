from dataclasses import dataclass, field
from typing import Optional, Union

from .entity_in_version_structure import VersionedChildStructure
from .luggage_spot_ref import LuggageSpotRef
from .passenger_spot_ref import PassengerSpotRef
from .passenger_vehicle_spot_ref import PassengerVehicleSpotRef
from .spot_sensor_ref import SpotSensorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorInSpotVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "SensorInSpot_VersionedChildStructure"

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
    spot_sensor_ref: Optional[SpotSensorRef] = field(
        default=None,
        metadata={
            "name": "SpotSensorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
