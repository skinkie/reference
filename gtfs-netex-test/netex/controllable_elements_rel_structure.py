from dataclasses import dataclass, field
from typing import List
from netex.controllable_element import ControllableElement
from netex.controllable_element_ref import ControllableElementRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElementsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of CONTROLLABLE ELEMENT PRICEs.
    """
    class Meta:
        name = "controllableElements_RelStructure"

    controllable_element_ref_or_controllable_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementRef",
                    "type": ControllableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElement",
                    "type": ControllableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
