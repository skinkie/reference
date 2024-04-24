from dataclasses import dataclass, field
from typing import List, Optional, Union

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .deck_vehicle_entrance_ref import DeckVehicleEntranceRef
from .entrance_setting_enumeration import EntranceSettingEnumeration
from .locatable_spot_refs_rel_structure import LocatableSpotRefsRelStructure
from .other_deck_entrance_ref import OtherDeckEntranceRef
from .passenger_entrance_ref import PassengerEntranceRef
from .train_component_ref import TrainComponentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "DeckEntranceAssignment_VersionStructure"

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
    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_setting: Optional[EntranceSettingEnumeration] = field(
        default=None,
        metadata={
            "name": "EntranceSetting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_spot: Optional[LocatableSpotRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "StartSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_spot: List[LocatableSpotRefsRelStructure] = field(
        default_factory=list,
        metadata={
            "name": "EndSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
