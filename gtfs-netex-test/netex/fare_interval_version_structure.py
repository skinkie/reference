from dataclasses import dataclass, field
from typing import Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareIntervalVersionStructure(PriceableObjectVersionStructure):
    """
    Type for FARE INTERVAL.

    :ivar name_of_class_of_unit: Name of implementation class associated
        with e.g. gDay, t.
    """
    class Meta:
        name = "FareInterval_VersionStructure"

    name_of_class_of_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        }
    )
