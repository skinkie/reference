from dataclasses import dataclass
from netex.vehicle_position_alignment_ref_structure import VehiclePositionAlignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePositionAlignmentRef(VehiclePositionAlignmentRefStructure):
    """
    Reference to a VEHICLE POSITION ALIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
