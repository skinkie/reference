from dataclasses import dataclass, field
from netex.vehicle_release_equipment_version_structure import VehicleReleaseEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleReleaseEquipment(VehicleReleaseEquipmentVersionStructure):
    """Specialisation of PLACE EQUIPMENT for VEHICLE RELEASE.

    +v1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
