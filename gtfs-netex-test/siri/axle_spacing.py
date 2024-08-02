from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AxleSpacing:
    axle_spacing: float = field(
        metadata={
            "name": "axleSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    axle_spacing_sequence_identifier: int = field(
        metadata={
            "name": "axleSpacingSequenceIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    axle_spacing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleSpacingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
