from dataclasses import dataclass
from .vehicle_pooling_service_version_structure import (
    VehiclePoolingServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiServiceVersionStructure(VehiclePoolingServiceVersionStructure):
    class Meta:
        name = "TaxiService_VersionStructure"
