from dataclasses import dataclass

from .site_element_ref_structure import SiteElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteRefStructure(SiteElementRefStructure):
    pass
