from dataclasses import dataclass, field
from netex.simple_vehicle_type_version_structure import SimpleVehicleTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleVehicleType(SimpleVehicleTypeVersionStructure):
    """
    A classification of personal use vehicles according to their properties,
    +v1.2.2.

    :ivar id: Identifier of PERSONAL TRANSPORT TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
