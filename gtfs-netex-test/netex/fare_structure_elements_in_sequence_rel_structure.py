from dataclasses import dataclass, field
from typing import List
from netex.controllable_element_in_sequence import ControllableElementInSequence
from netex.fare_structure_element_in_sequence import FareStructureElementInSequence
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementsInSequenceRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE STRUCTURE ELEMENT PRICEs.
    """
    class Meta:
        name = "fareStructureElementsInSequence_RelStructure"

    fare_structure_element_in_sequence_or_controllable_element_in_sequence: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareStructureElementInSequence",
                    "type": FareStructureElementInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementInSequence",
                    "type": ControllableElementInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
