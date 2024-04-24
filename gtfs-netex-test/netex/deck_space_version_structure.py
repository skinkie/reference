from dataclasses import dataclass, field
from typing import Optional

from .deck_component_version_structure import DeckComponentVersionStructure
from .deck_entrance_couples_rel_structure import DeckEntranceCouplesRelStructure
from .deck_entrance_usages_rel_structure import DeckEntranceUsagesRelStructure
from .deck_entrances_rel_structure import DeckEntrancesRelStructure
from .deck_space_capacities_rel_structure import DeckSpaceCapacitiesRelStructure
from .deck_space_ref_structure import DeckSpaceRefStructure
from .deck_windows_rel_structure import DeckWindowsRelStructure
from .type_of_deck_space_ref import TypeOfDeckSpaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckSpaceVersionStructure(DeckComponentVersionStructure):
    class Meta:
        name = "DeckSpace_VersionStructure"

    covered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    air_conditioned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioned",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoking_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmokingAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_deck_space_ref: Optional[TypeOfDeckSpaceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfDeckSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_deck_space_ref: Optional[DeckSpaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentDeckSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_entrances: Optional[DeckEntrancesRelStructure] = field(
        default=None,
        metadata={
            "name": "deckEntrances",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_entrance_couples: Optional[DeckEntranceCouplesRelStructure] = field(
        default=None,
        metadata={
            "name": "deckEntranceCouples",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_entrance_usages: Optional[DeckEntranceUsagesRelStructure] = field(
        default=None,
        metadata={
            "name": "deckEntranceUsages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_windows: Optional[DeckWindowsRelStructure] = field(
        default=None,
        metadata={
            "name": "deckWindows",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_space_capacities: Optional[DeckSpaceCapacitiesRelStructure] = field(
        default=None,
        metadata={
            "name": "deckSpaceCapacities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
