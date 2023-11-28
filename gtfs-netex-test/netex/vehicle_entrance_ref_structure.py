from dataclasses import dataclass
from netex.entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEntranceRefStructure(EntranceRefStructure):
    """
    Type for a reference to identifier of an VEHICLE ENTRANCE.
    """
