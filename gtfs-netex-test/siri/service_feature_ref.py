from dataclasses import dataclass

from .service_feature_ref_structure import ServiceFeatureRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceFeatureRef(ServiceFeatureRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
