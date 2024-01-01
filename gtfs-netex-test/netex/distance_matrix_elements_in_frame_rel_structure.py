from dataclasses import dataclass, field
from typing import List
from .distance_matrix_element import DistanceMatrixElement
from .frame_containment_structure import FrameContainmentStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "distanceMatrixElementsInFrame_RelStructure"

    distance_matrix_element: List[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
