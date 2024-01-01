from dataclasses import dataclass
from .activation_point_ref_structure import ActivationPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPointRef(ActivationPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
