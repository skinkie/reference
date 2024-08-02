from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .mobility_enum import MobilityEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Mobility:
    mobility_type: MobilityEnum = field(
        metadata={
            "name": "mobilityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    mobility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "mobilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
