from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntityStructure:
    """
    Type for ENTITY.

    :ivar name_of_class_attribute: Name of Class of the ENTITY. Allows
        reflection. Fixed for each ENTITY type.
    :ivar id: Identifier of ENTITY.
    """
    name_of_class_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
