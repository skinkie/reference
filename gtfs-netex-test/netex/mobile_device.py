from dataclasses import dataclass

from .mobile_device_version_structure import MobileDeviceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobileDevice(MobileDeviceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
