from dataclasses import dataclass

from .branding_version_structure import BrandingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Branding(BrandingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
