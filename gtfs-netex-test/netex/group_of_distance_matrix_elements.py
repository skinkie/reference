from dataclasses import dataclass

from .group_of_distance_matrix_elements_version_structure import GroupOfDistanceMatrixElementsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfDistanceMatrixElements(GroupOfDistanceMatrixElementsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
