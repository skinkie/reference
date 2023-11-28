from dataclasses import dataclass, field
from typing import List
from netex.distance_matrix_element import DistanceMatrixElement
from netex.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of DISTANCE MATRIX ELEMENTs.
    """
    class Meta:
        name = "distanceMatrixElementsInFrame_RelStructure"

    distance_matrix_element: List[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
