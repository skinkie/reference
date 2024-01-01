from dataclasses import dataclass, field
from typing import Optional
from .version_of_object_ref_structure import VersionOfObjectRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntityInVersionInFrameRefStructure(VersionOfObjectRefStructure):
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
