from dataclasses import dataclass

from .type_of_service_feature_ref_structure import TypeOfServiceFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfServiceFeatureRef(TypeOfServiceFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
