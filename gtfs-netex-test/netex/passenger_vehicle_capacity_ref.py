from dataclasses import dataclass

from .passenger_vehicle_capacity_ref_structure import PassengerVehicleCapacityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerVehicleCapacityRef(PassengerVehicleCapacityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
