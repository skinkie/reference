from dataclasses import dataclass
from netex.link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineLinkRefByValueStructure(LinkRefByValueStructure):
    """
    Type for a reference to a LINE LINK BY VALUE.
    """
