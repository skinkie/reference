from dataclasses import dataclass

from .passenger_vehicle_capacity_structure import PassengerVehicleCapacityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerVehicleCapacity(PassengerVehicleCapacityStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
