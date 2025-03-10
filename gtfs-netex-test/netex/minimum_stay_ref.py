from dataclasses import dataclass

from .minimum_stay_ref_structure import MinimumStayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MinimumStayRef(MinimumStayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
