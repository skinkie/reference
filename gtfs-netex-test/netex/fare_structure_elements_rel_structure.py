from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_structure_element import FareStructureElement
from .fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareStructureElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareStructureElements_RelStructure"

    fare_structure_element_ref_or_fare_structure_element: list[Union[FareStructureElementRef, FareStructureElement]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareStructureElementRef",
                    "type": FareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElement",
                    "type": FareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
