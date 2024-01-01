from dataclasses import dataclass
from .site_connection_ref_structure import SiteConnectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteConnectionRef(SiteConnectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
