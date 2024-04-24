from dataclasses import dataclass

from .spot_affinity_ref_structure import SpotAffinityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotAffinityRef(SpotAffinityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
