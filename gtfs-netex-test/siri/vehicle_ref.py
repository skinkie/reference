from dataclasses import dataclass

from .vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleRef(VehicleRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
