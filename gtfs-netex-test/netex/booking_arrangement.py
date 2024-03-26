from dataclasses import dataclass, field

from .booking_arrangement_version_structure import (
    BookingArrangementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingArrangement(BookingArrangementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
