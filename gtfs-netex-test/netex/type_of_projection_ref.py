from dataclasses import dataclass
from netex.type_of_projection_ref_structure import TypeOfProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfProjectionRef(TypeOfProjectionRefStructure):
    """
    Reference to a TYPE OF PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
