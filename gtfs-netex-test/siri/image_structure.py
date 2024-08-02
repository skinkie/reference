from dataclasses import dataclass, field
from typing import Optional, Union

from .image_content_enumeration import ImageContentEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ImageStructure:
    image_ref_or_image_binary: Optional[Union[str, bytes]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ImageRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ImageBinary",
                    "type": bytes,
                    "namespace": "http://www.siri.org.uk/siri",
                    "format": "base64",
                },
            ),
        },
    )
    image_content: Optional[ImageContentEnumeration] = field(
        default=None,
        metadata={
            "name": "ImageContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
