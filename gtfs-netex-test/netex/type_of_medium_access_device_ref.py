from dataclasses import dataclass
from netex.type_of_medium_access_device_ref_structure import TypeOfMediumAccessDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMediumAccessDeviceRef(TypeOfMediumAccessDeviceRefStructure):
    """Reference to a TYPE OF MEDIUM ACCESS DEVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
