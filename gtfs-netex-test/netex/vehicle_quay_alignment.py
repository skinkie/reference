from dataclasses import dataclass
from .vehicle_quay_alignment_version_structure import (
    VehicleQuayAlignmentVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleQuayAlignment(VehicleQuayAlignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
