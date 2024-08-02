from dataclasses import dataclass

from .service_features_delivery_structure import ServiceFeaturesDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceFeaturesDelivery(ServiceFeaturesDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
