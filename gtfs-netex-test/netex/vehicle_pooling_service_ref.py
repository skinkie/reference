from dataclasses import dataclass

from .vehicle_pooling_service_ref_structure import VehiclePoolingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingServiceRef(VehiclePoolingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
