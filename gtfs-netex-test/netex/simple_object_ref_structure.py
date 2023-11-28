from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleObjectRefStructure:
    """
    Type for a simple object reference.

    :ivar value:
    :ivar ref: Identifier of referenced entity.
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
