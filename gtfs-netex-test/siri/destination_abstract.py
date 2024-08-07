from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class DestinationAbstract:
    class Meta:
        name = "Destination"

    destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "destinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
