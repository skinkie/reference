from dataclasses import dataclass, field

from .vehicle_modes_of_transport_enumeration import VehicleModesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: VehicleModesOfTransportEnumeration = field(
        default=VehicleModesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
