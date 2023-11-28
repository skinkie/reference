from dataclasses import dataclass
from netex.type_of_service_feature_ref_structure import TypeOfServiceFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfServiceFeatureRef(TypeOfServiceFeatureRefStructure):
    """
    Reference to a TYPE OF SERVICE FEATURE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
