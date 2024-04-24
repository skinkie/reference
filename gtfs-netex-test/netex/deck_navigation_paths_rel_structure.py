from dataclasses import dataclass, field
from typing import List

from .deck_navigation_path import DeckNavigationPath
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckNavigationPathsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deckNavigationPaths_RelStructure"

    deck_navigation_path: List[DeckNavigationPath] = field(
        default_factory=list,
        metadata={
            "name": "DeckNavigationPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
