from dataclasses import dataclass, field


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleObjectRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    ref: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
