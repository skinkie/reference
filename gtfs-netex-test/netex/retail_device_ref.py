from dataclasses import dataclass
from netex.retail_device_ref_structure import RetailDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailDeviceRef(RetailDeviceRefStructure):
    """
    Reference to a RETAIL DEVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
