from dataclasses import dataclass, field

from .place_in_sequence import PlaceInSequence
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PlacesInSequenceRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "placesInSequence_RelStructure"

    place_in_sequence: list[PlaceInSequence] = field(
        default_factory=list,
        metadata={
            "name": "PlaceInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
