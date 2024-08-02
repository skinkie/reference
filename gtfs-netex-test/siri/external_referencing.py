from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class ExternalReferencing:
    external_location_code: str = field(
        metadata={
            "name": "externalLocationCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_system: str = field(
        metadata={
            "name": "externalReferencingSystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "externalReferencingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
