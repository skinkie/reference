from dataclasses import dataclass
from .stop_place_entrance_ref_structure import StopPlaceEntranceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceEntranceRef(StopPlaceEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
