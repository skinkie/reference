from dataclasses import dataclass

from .vehicle_orientation_relative_to_quay import VehicleOrientationRelativeToQuay

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DepartureOrientationRelativeToQuay(VehicleOrientationRelativeToQuay):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
