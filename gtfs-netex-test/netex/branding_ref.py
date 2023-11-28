from dataclasses import dataclass
from netex.branding_ref_structure import BrandingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BrandingRef(BrandingRefStructure):
    """
    Reference to a BRANDING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
