from dataclasses import dataclass

from .vehicle_features_delivery_structure import VehicleFeaturesDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleFeaturesDelivery(VehicleFeaturesDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
