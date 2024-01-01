from dataclasses import dataclass
from .vehicle_stopping_position_version_structure import (
    VehicleStoppingPositionVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPosition(VehicleStoppingPositionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: RestrictedVar
    url: RestrictedVar
    image: RestrictedVar
    postal_address: RestrictedVar
    road_address: RestrictedVar
