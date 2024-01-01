from dataclasses import dataclass
from .car_pooling_service_ref_structure import CarPoolingServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarPoolingServiceRef(CarPoolingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
