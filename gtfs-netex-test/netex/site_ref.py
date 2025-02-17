from dataclasses import dataclass

from .site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteRef(SiteRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
