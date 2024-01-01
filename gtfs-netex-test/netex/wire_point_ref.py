from dataclasses import dataclass
from .wire_point_ref_structure import WirePointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WirePointRef(WirePointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
