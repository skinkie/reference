from dataclasses import dataclass, field
from netex.type_of_medium_access_device_value_structure import TypeOfMediumAccessDeviceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMediumAccessDevice(TypeOfMediumAccessDeviceValueStructure):
    """A classification for a TYPE OF MEDIUM ACCESS DEVICE.

    +v1.2.2

    :ivar id: Identifier of TYPE OF MEDIUM ACCESS DEVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
