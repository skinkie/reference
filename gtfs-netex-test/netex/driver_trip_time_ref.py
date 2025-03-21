from dataclasses import dataclass

from .driver_trip_time_ref_structure import DriverTripTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DriverTripTimeRef(DriverTripTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
