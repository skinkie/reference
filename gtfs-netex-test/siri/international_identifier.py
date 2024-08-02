from dataclasses import dataclass, field
from typing import Optional

from .country_enum import CountryEnum
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class InternationalIdentifier:
    country: CountryEnum = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    national_identifier: str = field(
        metadata={
            "name": "nationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    international_identifier_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
