from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .location import Location

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class LocationByReference(Location):
    predefined_location_reference: str = field(
        metadata={
            "name": "predefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    location_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
