from dataclasses import dataclass
from netex.type_of_feature_ref_structure import TypeOfFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFeatureRef(TypeOfFeatureRefStructure):
    """
    Reference to a TYPE OF FEATURE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
