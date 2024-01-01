from dataclasses import dataclass
from .site_component_version_structure import SiteComponentVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestComponentVersionStructure(SiteComponentVersionStructure):
    class Meta:
        name = "PointOfInterestComponent_VersionStructure"
