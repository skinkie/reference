from dataclasses import dataclass, field
from typing import Optional

from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DeliveryVariantStructure:
    variant_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "VariantType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    content: NaturalLanguageStringStructure = field(
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
