from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CodespaceRefStructure:
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
