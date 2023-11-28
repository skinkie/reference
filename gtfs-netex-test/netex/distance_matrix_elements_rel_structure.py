from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.distance_matrix_element import DistanceMatrixElement
from netex.distance_matrix_element_ref import DistanceMatrixElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DISTANCE MATRIX ELEMENTs.
    """
    class Meta:
        name = "distanceMatrixElements_RelStructure"

    distance_matrix_element_ref_or_distance_matrix_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElement",
                    "type": DistanceMatrixElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
