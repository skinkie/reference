from dataclasses import dataclass

from .vehicle_occupancy_structure import VehicleOccupancyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ExpectedDepartureOccupancy(VehicleOccupancyStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
