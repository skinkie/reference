from dataclasses import dataclass
from netex.group_of_distance_matrix_elements_ref_structure_element import GroupOfDistanceMatrixElementsRefStructureElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfDistanceMatrixElementsRef(GroupOfDistanceMatrixElementsRefStructureElement):
    """
    Reference to a GROUP OF DISTANCE MATRIX ELEMENTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
