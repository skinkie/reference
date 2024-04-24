from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .other_deck_space import OtherDeckSpace
from .other_deck_space_ref import OtherDeckSpaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OtherDeckSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "otherDeckSpaces_RelStructure"

    other_deck_space_ref_or_other_deck_space: List[Union[OtherDeckSpaceRef, OtherDeckSpace]] = field(
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
                    "name": "OtherDeckSpace",
                    "type": OtherDeckSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
