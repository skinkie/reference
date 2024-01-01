from dataclasses import dataclass
from .retail_device_version_structure import RetailDeviceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDevice(RetailDeviceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
