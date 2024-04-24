from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotColumnVersionStructure(VersionedChildStructure):
    class Meta:
        name = "SpotColumn_VersionStructure"

    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    numbering_from_left: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NumberingFromLeft",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
