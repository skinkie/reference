from dataclasses import dataclass

from .stop_area_ref_structure import StopAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StopAreaRef(StopAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
