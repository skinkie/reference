from dataclasses import dataclass
from .stop_area_ref_structure import StopAreaRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAreaRef(StopAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
