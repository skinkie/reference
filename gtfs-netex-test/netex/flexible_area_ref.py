from dataclasses import dataclass
from .flexible_area_ref_structure import FlexibleAreaRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleAreaRef(FlexibleAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
