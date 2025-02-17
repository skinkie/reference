from dataclasses import dataclass

from .distance_matrix_element_version_structure import DistanceMatrixElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DynamicDistanceMatrixElementVersionStructure(DistanceMatrixElementVersionStructure):
    class Meta:
        name = "DynamicDistanceMatrixElement_VersionStructure"
