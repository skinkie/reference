from dataclasses import dataclass, field
from typing import List

from .abstract_discovery_delivery_structure import AbstractDiscoveryDeliveryStructure
from .service_feature import ServiceFeature

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceFeaturesDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    service_feature: List[ServiceFeature] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
