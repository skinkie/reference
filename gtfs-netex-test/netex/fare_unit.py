from dataclasses import dataclass, field
from typing import Optional
from netex.fare_unit_version_structure import FareUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareUnit(FareUnitVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.

    :ivar name_of_class: Name of Class of the ENTITY. Allows reflection.
        Fixed for each ENTITY type.
    :ivar id:
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
