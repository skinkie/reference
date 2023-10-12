from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ExternalObjectRefStructure:
    """
    Type for a reference.to an external object.

    :ivar value:
    :ivar type_value: Type of reference.
    :ivar ref: Reference to an entity in an external system.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    ref: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
