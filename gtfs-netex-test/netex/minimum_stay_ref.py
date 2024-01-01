from dataclasses import dataclass
from .minimum_stay_ref_structure import MinimumStayRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MinimumStayRef(MinimumStayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
