from dataclasses import dataclass, field
from netex.vehicle_service_part_version_structure import VehicleServicePartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePart(VehicleServicePartVersionStructure):
    """
    A part of a VEHICLE SERVICE composed of one or more BLOCKs and limited by
    periods spent at the GARAGE managing the vehicle in question.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
