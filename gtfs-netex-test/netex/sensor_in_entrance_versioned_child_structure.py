from dataclasses import dataclass, field
from typing import Optional, Union

from .deck_vehicle_entrance_ref import DeckVehicleEntranceRef
from .entity_in_version_structure import VersionedChildStructure
from .entrance_sensor_ref import EntranceSensorRef
from .other_deck_entrance_ref import OtherDeckEntranceRef
from .passenger_entrance_ref import PassengerEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorInEntranceVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "SensorInEntrance_VersionedChildStructure"

    deck_entrance_ref: Optional[Union[OtherDeckEntranceRef, DeckVehicleEntranceRef, PassengerEntranceRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OtherDeckEntranceRef",
                    "type": OtherDeckEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckVehicleEntranceRef",
                    "type": DeckVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEntranceRef",
                    "type": PassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    entrance_sensor_ref: Optional[EntranceSensorRef] = field(
        default=None,
        metadata={
            "name": "EntranceSensorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
