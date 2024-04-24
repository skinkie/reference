from dataclasses import dataclass

from .generic_path_link_ref_structure import GenericPathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OffSitePathLinkRefStructure(GenericPathLinkRefStructure):
    pass
