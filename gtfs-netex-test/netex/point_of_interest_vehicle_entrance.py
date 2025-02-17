from dataclasses import dataclass, field
from typing import Any

from .point_of_interest_vehicle_entrance_version_structure import PointOfInterestVehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestVehicleEntrance(PointOfInterestVehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
