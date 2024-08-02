from dataclasses import dataclass

from .service_features_discovery_request_structure import ServiceFeaturesDiscoveryRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceFeaturesRequest(ServiceFeaturesDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
