from dataclasses import dataclass
from netex.entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceVehicleEntranceRefStructure(EntranceRefStructure):
    """
    Type for reference to a STOP PLACE VEHICLE  ENTRANCE.
    """
