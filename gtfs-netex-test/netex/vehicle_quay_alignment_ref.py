from dataclasses import dataclass
from netex.vehicle_quay_alignment_ref_structure import VehicleQuayAlignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleQuayAlignmentRef(VehicleQuayAlignmentRefStructure):
    """
    Reference to a VEHICLE QUAY ALIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
