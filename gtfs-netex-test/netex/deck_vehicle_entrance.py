from dataclasses import dataclass

from .deck_vehicle_entrance_version_structure import DeckVehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckVehicleEntrance(DeckVehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
