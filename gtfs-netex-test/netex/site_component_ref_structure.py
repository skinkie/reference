from dataclasses import dataclass
from netex.site_element_ref_structure import SiteElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteComponentRefStructure(SiteElementRefStructure):
    """
    Type for reference to a SITE COMPONENT.
    """
