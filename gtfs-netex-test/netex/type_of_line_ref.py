from dataclasses import dataclass
from netex.type_of_line_ref_structure import TypeOfLineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfLineRef(TypeOfLineRefStructure):
    """
    Reference to a TYPE OF LINE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
