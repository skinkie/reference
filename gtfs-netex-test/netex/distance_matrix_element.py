from dataclasses import dataclass, field
from netex.distance_matrix_element_version_structure import DistanceMatrixElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElement(DistanceMatrixElementVersionStructure):
    """
    A cell of an origin-destination matrix for TARIFF ZONEs or STOP POINTs,
    expressing a fare distance for the corresponding trip: value in km, number of
    fare units etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
