from dataclasses import dataclass
from .point_of_interest_vehicle_entrance_ref_structure import (
    PointOfInterestVehicleEntranceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestVehicleEntranceRef(
    PointOfInterestVehicleEntranceRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
