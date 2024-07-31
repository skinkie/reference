from dataclasses import dataclass, field
from typing import List, Optional, Union

from .deck_vehicle_entrance_ref import DeckVehicleEntranceRef
from .entity_in_version_structure import VersionedChildStructure
from .entrance_setting_enumeration import EntranceSettingEnumeration
from .entrance_usage_enumeration import EntranceUsageEnumeration
from .locatable_spot_range_ref_structure import LocatableSpotRangeRefStructure
from .multilingual_string import MultilingualString
from .other_deck_entrance_ref import OtherDeckEntranceRef
from .passenger_entrance_ref import PassengerEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckEntranceUsageVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "DeckEntranceUsage_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_usage_type: Optional[EntranceUsageEnumeration] = field(
        default=None,
        metadata={
            "name": "EntranceUsageType",
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
    controlled_locking: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ControlledLocking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    start_spot: Optional[LocatableSpotRangeRefStructure] = field(
        default=None,
        metadata={
            "name": "StartSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_spot: List[LocatableSpotRangeRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "EndSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
