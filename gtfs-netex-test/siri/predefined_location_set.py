from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .multilingual_string import MultilingualString
from .predefined_location import PredefinedLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class PredefinedLocationSet:
    predefined_location_set_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location_set_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location: List[PredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    predefined_location_set_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
