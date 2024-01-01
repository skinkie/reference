from dataclasses import dataclass
from .site_component_ref_structure import SiteComponentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteComponentRef(SiteComponentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
