from dataclasses import dataclass
from netex.link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkRefByValue(LinkRefByValueStructure):
    """
    Reference to a LINK using its end values.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
