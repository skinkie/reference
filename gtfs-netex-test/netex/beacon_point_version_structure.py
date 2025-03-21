from dataclasses import dataclass

from .activation_point_version_structure import ActivationPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BeaconPointVersionStructure(ActivationPointVersionStructure):
    class Meta:
        name = "BeaconPoint_VersionStructure"
