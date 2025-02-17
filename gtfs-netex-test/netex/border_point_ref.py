from dataclasses import dataclass

from .border_point_ref_structure import BorderPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BorderPointRef(BorderPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
