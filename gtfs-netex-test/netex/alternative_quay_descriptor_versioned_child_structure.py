from dataclasses import dataclass, field
from typing import Optional
from .alternative_name_versioned_child_structure import (
    AlternativeNameVersionedChildStructure,
)
from .multilingual_string import MultilingualString


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeQuayDescriptorVersionedChildStructure(
    AlternativeNameVersionedChildStructure
):
    class Meta:
        name = "AlternativeQuayDescriptor_VersionedChildStructure"

    cross_road: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CrossRoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    landmark: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Landmark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
