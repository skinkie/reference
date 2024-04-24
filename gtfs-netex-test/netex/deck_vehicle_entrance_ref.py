from dataclasses import dataclass

from .deck_vehicle_entrance_ref_structure import DeckVehicleEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckVehicleEntranceRef(DeckVehicleEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
