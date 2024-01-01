from dataclasses import dataclass
from .flexible_area_version_structure import FlexibleAreaVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleArea(FlexibleAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
