from dataclasses import dataclass
from .type_of_feature_value_structure import TypeOfFeatureValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFeature(TypeOfFeatureValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
