from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .type_of_locatable_spot_enumeration import TypeOfLocatableSpotEnumeration
from .type_of_locatable_spot_ref import TypeOfLocatableSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckSpaceCapacityVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "DeckSpaceCapacity_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locatable_spot_type: Optional[TypeOfLocatableSpotEnumeration] = field(
        default=None,
        metadata={
            "name": "LocatableSpotType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_locatable_spot_ref: Optional[TypeOfLocatableSpotRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLocatableSpotRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Capacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
