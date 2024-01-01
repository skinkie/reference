from dataclasses import dataclass
from .flexible_line_derived_view_structure import (
    FlexibleLineDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineView(FlexibleLineDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
