from dataclasses import dataclass
from .line_derived_view_structure import LineDerivedViewStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineView(LineDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
