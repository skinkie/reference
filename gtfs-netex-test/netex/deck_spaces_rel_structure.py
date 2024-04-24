from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .other_deck_space import OtherDeckSpace
from .other_deck_space_ref import OtherDeckSpaceRef
from .passenger_space import PassengerSpace
from .passenger_space_ref import PassengerSpaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "deckSpaces_RelStructure"

    deck_space_ref_or_deck_space: List[Union[OtherDeckSpaceRef, PassengerSpaceRef, OtherDeckSpace, PassengerSpace]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "OtherDeckSpace",
                    "type": OtherDeckSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpace",
                    "type": PassengerSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
