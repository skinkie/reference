from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .payload_publication import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class GenericPublication(PayloadPublication):
    generic_publication_name: str = field(
        metadata={
            "name": "genericPublicationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    generic_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "genericPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
