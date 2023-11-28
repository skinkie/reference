from dataclasses import dataclass
from netex.simple_object_ref_structure import SimpleObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleObjectRef(SimpleObjectRefStructure):
    """
    Simple unversioned reference to a NeTEx ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
