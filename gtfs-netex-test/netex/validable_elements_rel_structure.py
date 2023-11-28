from dataclasses import dataclass, field
from typing import List
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.validable_element import ValidableElement
from netex.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidableElementsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE PRODUCT PRICEs.
    """
    class Meta:
        name = "validableElements_RelStructure"

    validable_element_ref_or_validable_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ValidableElementRef",
                    "type": ValidableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElement",
                    "type": ValidableElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
