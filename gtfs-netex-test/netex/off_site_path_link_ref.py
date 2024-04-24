from dataclasses import dataclass

from .off_site_path_link_ref_structure import OffSitePathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OffSitePathLinkRef(OffSitePathLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
