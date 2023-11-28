from dataclasses import dataclass
from netex.car_pooling_service_ref_structure import CarPoolingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarPoolingServiceRef(CarPoolingServiceRefStructure):
    """Identifier of an CAR POOLING SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
