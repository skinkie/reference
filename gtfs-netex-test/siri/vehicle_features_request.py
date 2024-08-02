from dataclasses import dataclass

from .vehicle_features_request_structure import VehicleFeaturesRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleFeaturesRequest(VehicleFeaturesRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
