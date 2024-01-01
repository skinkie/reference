from dataclasses import dataclass
from .vehicle_position_alignment_ref_structure import (
    VehiclePositionAlignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePositionAlignmentRef(VehiclePositionAlignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
