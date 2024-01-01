from dataclasses import dataclass
from .zone_projection_version_structure import ZoneProjectionVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZoneProjection(ZoneProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
