from dataclasses import dataclass

from .passenger_vehicle_spot_version_structure import PassengerVehicleSpotVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerVehicleSpot(PassengerVehicleSpotVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
