from dataclasses import dataclass

from .entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceVehicleEntranceRefStructure(EntranceRefStructure):
    pass
