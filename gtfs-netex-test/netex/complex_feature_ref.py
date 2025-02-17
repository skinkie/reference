from dataclasses import dataclass

from .complex_feature_ref_structure import ComplexFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ComplexFeatureRef(ComplexFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
