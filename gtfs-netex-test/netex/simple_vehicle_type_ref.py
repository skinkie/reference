from dataclasses import dataclass

from .simple_vehicle_type_ref_structure import SimpleVehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleVehicleTypeRef(SimpleVehicleTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
