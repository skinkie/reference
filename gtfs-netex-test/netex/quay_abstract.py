from dataclasses import dataclass

from .site_version_structure import SiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayAbstract(SiteVersionStructure):
    class Meta:
        name = "Quay_"
        namespace = "http://www.netex.org.uk/netex"
