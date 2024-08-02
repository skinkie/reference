from dataclasses import dataclass

from .entrance_to_vehicle_ref_structure import EntranceToVehicleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EntranceToVehicleRef(EntranceToVehicleRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
