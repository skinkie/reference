from dataclasses import dataclass

from .site_connection_version_structure import SiteConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteConnection(SiteConnectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
