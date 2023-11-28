from dataclasses import dataclass
from netex.distance_matrix_element_ref_structure import DistanceMatrixElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementInverseRef(DistanceMatrixElementRefStructure):
    """
    Reference to a DISTANCE MATRIX ELEMENT, used in a backwards direction.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
