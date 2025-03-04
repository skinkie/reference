from dataclasses import dataclass

from .rental_availability_version_structure import RentalAvailabilityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RentalAvailability(RentalAvailabilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
