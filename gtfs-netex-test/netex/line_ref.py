from dataclasses import dataclass
from netex.line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineRef(LineRefStructure):
    """
    Reference to a LINE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
