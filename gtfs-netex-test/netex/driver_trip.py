from dataclasses import dataclass, field
from netex.driver_trip_version_structure import DriverTripVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverTrip(DriverTripVersionStructure):
    """A planned non-driving movement of a driver within a DUTY PART.

    This may be necessary to reach the first SPELL in a STRETCH, between
    two SPELLs or after the last SPELL in a STRETCH. It may be entirely
    on foot or may use a VEHICLE JOURNEY on a vehicle driven by another
    driver.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
