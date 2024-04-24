from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotRowVersionStructure(VersionedChildStructure):
    class Meta:
        name = "SpotRow_VersionStructure"

    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    numbering_from_front: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NumberingFromFront",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
