from dataclasses import dataclass
from .stop_area_version_structure import StopAreaVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopArea(StopAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
