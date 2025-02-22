from dataclasses import dataclass

from .headway_ref_structure import HeadwayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class HeadwayRef(HeadwayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
