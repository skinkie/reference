from dataclasses import dataclass
from netex.complex_feature_ref_structure import ComplexFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplexFeatureRef(ComplexFeatureRefStructure):
    """
    Reference to a COMPLEX FEATURE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
