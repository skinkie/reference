from dataclasses import dataclass, field
from netex.simple_feature_version_structure import SimpleFeatureVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleFeature(SimpleFeatureVersionStructure):
    """
    An abstract representation of elementary objects related to the spatial
    representation of the network POINTs (0-dimensional objects), LINKs
    (1-dimensional objects) and ZONEs (2-dimensional objects) may be viewed as
    SIMPLE FEATUREs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
