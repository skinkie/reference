from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_name_versioned_child_structure import AlternativeNameVersionedChildStructure
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeQuayDescriptorVersionedChildStructure(AlternativeNameVersionedChildStructure):
    """
    Type for a STOP PLACE COMPONENT.

    :ivar cross_road: Name of a Road that crosses the Road the street
        near the SITE ELEMENT that can be used to describe its relative
        location.
    :ivar landmark: Name of a Landmark near the SITE ELEMENT that can be
        used to describe its relative location.
    """
    class Meta:
        name = "AlternativeQuayDescriptor_VersionedChildStructure"

    cross_road: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CrossRoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    landmark: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Landmark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
