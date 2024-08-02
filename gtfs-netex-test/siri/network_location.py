from dataclasses import dataclass, field
from typing import Optional

from .destination_abstract import DestinationAbstract
from .extension_type import ExtensionType
from .location import Location
from .supplementary_positional_description import SupplementaryPositionalDescription

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class NetworkLocation(Location):
    supplementary_positional_description: Optional[SupplementaryPositionalDescription] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    destination: Optional[DestinationAbstract] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    network_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
