from dataclasses import dataclass, field
from typing import Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareUnitVersionStructure(PriceableObjectVersionStructure):
    """
    Type for FARE UNIT.

    :ivar name_of_class_of_unit: Name of class associated with UNIT.
    """
    class Meta:
        name = "FareUnit_VersionStructure"

    name_of_class_of_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        }
    )
