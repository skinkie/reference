from dataclasses import dataclass
from netex.line_derived_view_structure import LineDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineView(LineDerivedViewStructure):
    """
    Simplified view of a LINE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
