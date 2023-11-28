from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespaceRefStructure:
    """
    Type for a reference to a CODESPACE.

    :ivar value:
    :ivar ref: Identifier of CODESPACE i.e. namespace of identifiers.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    ref: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
