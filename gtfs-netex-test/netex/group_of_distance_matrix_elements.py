from dataclasses import dataclass, field
from netex.group_of_distance_matrix_elements_version_structure import GroupOfDistanceMatrixElementsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfDistanceMatrixElements(GroupOfDistanceMatrixElementsVersionStructure):
    """
    A group of DISTANCE MATRIX ELEMENTs; may set common properties for a given set
    of origin and destination pairs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
