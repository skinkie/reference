from dataclasses import dataclass, field
from netex.type_of_service_feature_value_structure import TypeOfServiceFeatureValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfServiceFeature(TypeOfServiceFeatureValueStructure):
    """
    Classification of TYPE OF SERVICE FEATURE.

    :ivar id: Reference to a TYPE OF SERVICE FEATURE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
