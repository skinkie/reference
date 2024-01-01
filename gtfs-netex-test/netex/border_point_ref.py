from dataclasses import dataclass
from .border_point_ref_structure import BorderPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointRef(BorderPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
