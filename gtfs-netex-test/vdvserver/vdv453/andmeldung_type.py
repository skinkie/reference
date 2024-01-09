from dataclasses import dataclass, field
from typing import List, Type
from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class AndmeldungType:
    class Meta:
        name = "ANDMeldungType"

    zst: XmlDateTime = field(
        metadata={
            "name": "Zst",
            "type": "Attribute",
            "required": True,
        }
    )
    verfall_zst: XmlDateTime = field(
        metadata={
            "name": "VerfallZst",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "KanalID",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "MeldungsID",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "FormatID",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "MessageXML",
                    "type": Type["AndmeldungType.MessageXml"],
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class MessageXml:
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "process_contents": "skip",
            },
        )
