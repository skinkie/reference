from dataclasses import dataclass
from netex.medium_access_device_ref_structure import MediumAccessDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobileDeviceRefStructure(MediumAccessDeviceRefStructure):
    """
    Type for a reference to a MOBILE DEVICE.
    """
