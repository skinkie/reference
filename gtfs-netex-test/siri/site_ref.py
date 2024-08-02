from dataclasses import dataclass

from .site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SiteRef(SiteRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
