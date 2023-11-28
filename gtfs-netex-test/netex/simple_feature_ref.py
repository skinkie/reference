from dataclasses import dataclass
from netex.simple_feature_ref_structure import SimpleFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleFeatureRef(SimpleFeatureRefStructure):
    """
    Reference to a SIMPLE FEATURE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
