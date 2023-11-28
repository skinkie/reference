from dataclasses import dataclass
from netex.ordered_version_of_object_ref_structure import OrderedVersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrderedVersionOfObjectRef(OrderedVersionOfObjectRefStructure):
    """Reference to a NeTEx Object i.e. concrete instance of an ENTITY may include
    a version.

    Implements a one to one relationship by reference.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
