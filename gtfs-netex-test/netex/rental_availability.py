from dataclasses import dataclass, field
from netex.rental_availability_version_structure import RentalAvailabilityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalAvailability(RentalAvailabilityVersionStructure):
    """A summary of the status of the rental at a  SITE  at a given point on time.

    +v1.2.2

    :ivar id: Identifier of RENTAL AVAILABILITYS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
