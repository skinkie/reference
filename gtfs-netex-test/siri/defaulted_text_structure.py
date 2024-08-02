from dataclasses import dataclass, field

from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DefaultedTextStructure(NaturalLanguageStringStructure):
    overridden: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
