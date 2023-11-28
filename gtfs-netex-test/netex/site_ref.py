from dataclasses import dataclass
from netex.site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteRef(SiteRefStructure):
    """
    Reference to a SITE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
