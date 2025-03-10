from dataclasses import dataclass

from .info_link_structure import InfoLinkStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InfoLink(InfoLinkStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
