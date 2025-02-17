from dataclasses import dataclass

from .entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingEntranceRefStructure(EntranceRefStructure):
    pass
