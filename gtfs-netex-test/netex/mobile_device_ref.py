from dataclasses import dataclass
from netex.mobile_device_ref_structure import MobileDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobileDeviceRef(MobileDeviceRefStructure):
    """Reference to a MOBILE DEVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
