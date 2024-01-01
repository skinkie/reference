from dataclasses import dataclass
from .monitored_vehicle_sharing_parking_bay_ref_structure import (
    MonitoredVehicleSharingParkingBayRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonitoredVehicleSharingParkingBayRef(
    MonitoredVehicleSharingParkingBayRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
