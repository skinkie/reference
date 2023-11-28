from dataclasses import dataclass
from netex.distance_matrix_element_derived_view_structure import DistanceMatrixElementDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementView(DistanceMatrixElementDerivedViewStructure):
    """
    Simplified  view of CONNECTING JOURNEY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
