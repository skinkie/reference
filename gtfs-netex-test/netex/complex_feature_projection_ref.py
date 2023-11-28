from dataclasses import dataclass
from netex.complex_feature_projection_ref_structure import ComplexFeatureProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplexFeatureProjectionRef(ComplexFeatureProjectionRefStructure):
    """
    Reference to a COMPLEX FEATURE PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
