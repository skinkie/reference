from dataclasses import dataclass

from .spot_affinity_version_structure import SpotAffinityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotAffinity(SpotAffinityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
