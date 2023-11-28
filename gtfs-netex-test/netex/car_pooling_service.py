from dataclasses import dataclass, field
from netex.car_pooling_service_version_structure import CarPoolingServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarPoolingService(CarPoolingServiceVersionStructure):
    """A transport service that connects users (driver and passenger(s)) for
    carrying out trips.

    +v1.2.2

    :ivar id: Identifier of GENERAL POOLIMG SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
