from dataclasses import dataclass

from .parking_bay_status_ref_structure import ParkingBayStatusRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RentalAvailabilityRef(ParkingBayStatusRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
