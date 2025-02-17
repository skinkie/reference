from dataclasses import dataclass

from .retail_device_version_structure import RetailDeviceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RetailDevice(RetailDeviceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
