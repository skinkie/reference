from dataclasses import dataclass
from netex.path_link_ref_by_value_structure import PathLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkRefByValue(PathLinkRefByValueStructure):
    """
    Reference to a PATH LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
