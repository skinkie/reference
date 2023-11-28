from dataclasses import dataclass
from netex.activation_point_version_structure import ActivationPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BeaconPointVersionStructure(ActivationPointVersionStructure):
    """
    Type for BEACON POINT.
    """
    class Meta:
        name = "BeaconPoint_VersionStructure"
