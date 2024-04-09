from dataclasses import dataclass

from .dynamic_distance_matrix_element_version_structure import DynamicDistanceMatrixElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicDistanceMatrixElement(DynamicDistanceMatrixElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
