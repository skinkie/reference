from dataclasses import dataclass
from netex.class_ref_structure import ClassRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassRef(ClassRefStructure):
    """
    Reference to a Type of an ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
