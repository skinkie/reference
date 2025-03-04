from dataclasses import dataclass, field
from typing import Union

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .validable_element import ValidableElement
from .validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidableElementsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "validableElements_RelStructure"

    validable_element_ref_or_validable_element: list[Union[ValidableElementRef, ValidableElement]] = field(
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
        },
    )
