from dataclasses import dataclass, field
from netex.type_of_feature_value_structure import TypeOfFeatureValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFeature(TypeOfFeatureValueStructure):
    """
    TYPE OF FEATURe.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
