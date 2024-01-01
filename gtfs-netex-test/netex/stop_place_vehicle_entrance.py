from dataclasses import dataclass
from .stop_place_vehicle_entrance_version_structure import (
    StopPlaceVehicleEntranceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceVehicleEntrance(StopPlaceVehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: RestrictedVar
