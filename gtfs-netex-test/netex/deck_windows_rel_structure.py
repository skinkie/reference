from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_window import DeckWindow
from .deck_window_ref import DeckWindowRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckWindowsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckWindows_RelStructure"

    deck_window_ref_or_deck_window: List[Union[DeckWindowRef, DeckWindow]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeckWindowRef",
                    "type": DeckWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckWindow",
                    "type": DeckWindow,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
