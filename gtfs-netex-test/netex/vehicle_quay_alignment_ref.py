from dataclasses import dataclass
from .vehicle_quay_alignment_ref_structure import (
    VehicleQuayAlignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleQuayAlignmentRef(VehicleQuayAlignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
