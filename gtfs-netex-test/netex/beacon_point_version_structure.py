from dataclasses import dataclass
from .activation_point_version_structure import ActivationPointVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BeaconPointVersionStructure(ActivationPointVersionStructure):
    class Meta:
        name = "BeaconPoint_VersionStructure"
