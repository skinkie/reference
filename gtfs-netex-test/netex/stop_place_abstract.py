from dataclasses import dataclass

from .site_version_structure import SiteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StopPlaceAbstract(SiteVersionStructure):
    class Meta:
        name = "StopPlace_"
        namespace = "http://www.netex.org.uk/netex"
