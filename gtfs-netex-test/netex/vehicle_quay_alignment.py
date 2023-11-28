from dataclasses import dataclass, field
from netex.vehicle_quay_alignment_version_structure import VehicleQuayAlignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleQuayAlignment(VehicleQuayAlignmentVersionStructure):
    """
    Designated Position within a VEHICLE STOPPING PLACE for a Vehicle to stop.

    :ivar id: Identifier of VEHICLE QUAY ALIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
