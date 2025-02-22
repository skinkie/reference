from dataclasses import dataclass

from .simple_feature_version_structure import SimpleFeatureVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SimpleFeature(SimpleFeatureVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
