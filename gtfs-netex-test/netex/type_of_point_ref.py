from dataclasses import dataclass
from netex.type_of_point_ref_structure import TypeOfPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPointRef(TypeOfPointRefStructure):
    """
    Reference to a TYPE OF POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
