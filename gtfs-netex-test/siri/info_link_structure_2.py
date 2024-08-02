from dataclasses import dataclass, field
from typing import List, Optional

from .image_structure import ImageStructure
from .link_content_enumeration import LinkContentEnumeration
from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoLinkStructure2:
    class Meta:
        name = "InfoLinkStructure"

    uri: str = field(
        metadata={
            "name": "Uri",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    label: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    image: Optional[ImageStructure] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_content: Optional[LinkContentEnumeration] = field(
        default=None,
        metadata={
            "name": "LinkContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
