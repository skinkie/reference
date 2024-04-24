from dataclasses import dataclass

from .passenger_vehicle_spot_ref_structure import PassengerVehicleSpotRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerVehicleSpotRef(PassengerVehicleSpotRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
