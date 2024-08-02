from dataclasses import dataclass

from .service_feature_structure import ServiceFeatureStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceFeature(ServiceFeatureStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
