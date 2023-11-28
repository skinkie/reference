from dataclasses import dataclass
from netex.info_link_structure import InfoLinkStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfoLink(InfoLinkStructure):
    """
    A hyperlink to an external web resource.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
