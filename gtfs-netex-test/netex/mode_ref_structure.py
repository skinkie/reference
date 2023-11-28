from dataclasses import dataclass, field
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModeRefStructure(SubmodeRefStructure):
    """
    Type for a reference to a MODE and SUBMODE.
    """
    mode: AllVehicleModesOfTransportEnumeration = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
