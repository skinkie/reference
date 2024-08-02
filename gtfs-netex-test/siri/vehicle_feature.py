from dataclasses import dataclass

from .vehicle_features_structure import VehicleFeaturesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleFeature(VehicleFeaturesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
