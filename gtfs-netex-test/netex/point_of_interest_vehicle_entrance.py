from dataclasses import dataclass
from .point_of_interest_vehicle_entrance_version_structure import (
    PointOfInterestVehicleEntranceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestVehicleEntrance(
    PointOfInterestVehicleEntranceVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: RestrictedVar
