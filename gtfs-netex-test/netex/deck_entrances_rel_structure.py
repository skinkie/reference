from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_vehicle_entrance import DeckVehicleEntrance
from .deck_vehicle_entrance_ref import DeckVehicleEntranceRef
from .other_deck_entrance import OtherDeckEntrance
from .other_deck_entrance_ref import OtherDeckEntranceRef
from .passenger_entrance import PassengerEntrance
from .passenger_entrance_ref import PassengerEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntrancesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckEntrances_RelStructure"

    deck_entrance_ref_or_deck_entrance: List[Union[OtherDeckEntranceRef, DeckVehicleEntranceRef, PassengerEntranceRef, OtherDeckEntrance, DeckVehicleEntrance, PassengerEntrance]] = field(
        default_factory=list,
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
                {
                    "name": "OtherDeckEntrance",
                    "type": OtherDeckEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckVehicleEntrance",
                    "type": DeckVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEntrance",
                    "type": PassengerEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
