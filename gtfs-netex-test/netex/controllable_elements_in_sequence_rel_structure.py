from dataclasses import dataclass, field
from typing import List
from netex.controllable_element_in_sequence import ControllableElementInSequence
from netex.controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementsInSequenceRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CONTROLLABLE ELEMENT IN SEQUENCEs.
    """
    class Meta:
        name = "controllableElementsInSequence_RelStructure"

    controllable_element_in_sequence_ref_or_controllable_element_in_sequence: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
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
