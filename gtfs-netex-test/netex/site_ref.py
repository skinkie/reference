from dataclasses import dataclass
from .site_ref_structure import SiteRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteRef(SiteRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
