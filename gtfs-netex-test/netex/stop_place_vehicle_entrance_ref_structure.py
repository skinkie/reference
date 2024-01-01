from dataclasses import dataclass
from .entrance_ref_structure import EntranceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceVehicleEntranceRefStructure(EntranceRefStructure):
    value: RestrictedVar
