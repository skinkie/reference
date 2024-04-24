from dataclasses import dataclass, field
from typing import Optional, Union

from .deck_level_ref import DeckLevelRef
from .deck_path_junction_ref import DeckPathJunctionRef
from .deck_ref import DeckRef
from .deck_vehicle_entrance_ref import DeckVehicleEntranceRef
from .deck_window_ref import DeckWindowRef
from .luggage_spot_ref import LuggageSpotRef
from .other_deck_entrance_ref import OtherDeckEntranceRef
from .other_deck_space_ref import OtherDeckSpaceRef
from .passenger_entrance_ref import PassengerEntranceRef
from .passenger_space_ref import PassengerSpaceRef
from .passenger_spot_ref import PassengerSpotRef
from .passenger_vehicle_spot_ref import PassengerVehicleSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPathLinkEndStructure:
    deck_ref: Optional[DeckRef] = field(
        default=None,
        metadata={
            "name": "DeckRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_level_ref: Optional[DeckLevelRef] = field(
        default=None,
        metadata={
            "name": "DeckLevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_component_ref_or_deck_entrance_ref_or_deck_space_ref_or_locatable_spot_ref: Optional[Union[DeckWindowRef, OtherDeckEntranceRef, DeckVehicleEntranceRef, PassengerEntranceRef, OtherDeckSpaceRef, PassengerSpaceRef, LuggageSpotRef, PassengerVehicleSpotRef, PassengerSpotRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeckWindowRef",
                    "type": DeckWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "OtherDeckSpaceRef",
                    "type": OtherDeckSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpaceRef",
                    "type": PassengerSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
    deck_path_junction_ref: Optional[DeckPathJunctionRef] = field(
        default=None,
        metadata={
            "name": "DeckPathJunctionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
