from dataclasses import dataclass, field
from typing import Optional

from .deck_levels_rel_structure import DeckLevelsRelStructure
from .decks_rel_structure import DecksRelStructure
from .entity_in_version_structure import (
    DataManagedObjectStructure,
    ValidityConditionsRelStructure,
)
from .multilingual_string import MultilingualString
from .vehicle_orientation_enumeration import VehicleOrientationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlanVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "DeckPlan_VersionStructure"

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
    orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    configuration_conditions: Optional[ValidityConditionsRelStructure] = field(
        default=None,
        metadata={
            "name": "configurationConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_levels: Optional[DeckLevelsRelStructure] = field(
        default=None,
        metadata={
            "name": "deckLevels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    decks: Optional[DecksRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
