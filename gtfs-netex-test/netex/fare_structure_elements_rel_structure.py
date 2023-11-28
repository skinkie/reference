from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fare_structure_element import FareStructureElement
from netex.fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE STRUCTURE ELEMENTs.
    """
    class Meta:
        name = "fareStructureElements_RelStructure"

    fare_structure_element_ref_or_fare_structure_element: List[object] = field(
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
        }
    )
