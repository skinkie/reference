from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.direction_ref import DirectionRef
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DirectionDerivedViewStructure(DerivedViewStructure):
    """
    Type for DIRECTION VIEW.

    :ivar direction_ref:
    :ivar name: Name of DIRECTION.
    """
    class Meta:
        name = "Direction_DerivedViewStructure"

    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
