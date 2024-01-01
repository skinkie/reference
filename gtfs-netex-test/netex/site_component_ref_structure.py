from dataclasses import dataclass
from .site_element_ref_structure import SiteElementRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteComponentRefStructure(SiteElementRefStructure):
    value: RestrictedVar
