from dataclasses import dataclass
from netex.line_link_ref_by_value_structure import LineLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineLinkRefByValue(LineLinkRefByValueStructure):
    """
    Reference to a LINE LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
