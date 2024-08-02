from dataclasses import dataclass

from .feature_ref_structure_2 import FeatureRefStructure2

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FeatureRef(FeatureRefStructure2):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
