from dataclasses import dataclass

from .car_pooling_service_ref_structure import CarPoolingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CarPoolingServiceRef(CarPoolingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
