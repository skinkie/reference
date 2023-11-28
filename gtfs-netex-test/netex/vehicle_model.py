from dataclasses import dataclass, field
from netex.vehicle_model_version_structure import VehicleModelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleModel(VehicleModelVersionStructure):
    """
    A classification of public transport vehicles according to the vehicle
    scheduling requirements in MODE and capacity (e.g. standard bus, double-deck,
    ...).

    :ivar id: Identifier of VEHICLE MODEL.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
