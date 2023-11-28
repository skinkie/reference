from dataclasses import dataclass, field
from netex.vehicle_position_alignment_version_structure import VehiclePositionAlignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePositionAlignment(VehiclePositionAlignmentVersionStructure):
    """
    Designated Position within a VEHICLE STOPPING PLACE for a Vehicle to stop.

    :ivar id: Identifier of VEHICLE POSTION ALIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
