from dataclasses import dataclass

from .complex_feature_version_structure import ComplexFeatureVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ComplexFeature(ComplexFeatureVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
