from dataclasses import dataclass
from .flexible_line_ref_structure import FlexibleLineRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineRef(FlexibleLineRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
