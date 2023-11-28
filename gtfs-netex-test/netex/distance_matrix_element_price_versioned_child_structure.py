from dataclasses import dataclass, field
from typing import Optional
from netex.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a DISTANCE MATRIX ELEMENT PRICEs.
    """
    class Meta:
        name = "DistanceMatrixElementPrice_VersionedChildStructure"

    distance_matrix_element_ref_or_group_of_distance_matrix_elements_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
