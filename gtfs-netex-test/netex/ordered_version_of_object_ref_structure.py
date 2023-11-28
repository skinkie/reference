from dataclasses import dataclass, field
from typing import Optional
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrderedVersionOfObjectRefStructure(VersionOfObjectRefStructure):
    """
    Type for a versioned reference to a NeTEx Object.

    :ivar order: Order of element.
    """
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
