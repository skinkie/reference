from dataclasses import dataclass, field
from netex.chauffeured_vehicle_service_version_structure import ChauffeuredVehicleServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChauffeuredVehicleService(ChauffeuredVehicleServiceVersionStructure):
    """A type of VEHICLE POOLING SERVICE which can only be used by prior
    arrangement and where the driver has a commercial agreement with the user.

    +v1.2.2

    :ivar id: Identifier of CHAUFFEURED VEHICLE SERVICE
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
