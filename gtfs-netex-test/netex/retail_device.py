from dataclasses import dataclass, field
from netex.retail_device_version_structure import RetailDeviceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailDevice(RetailDeviceVersionStructure):
    """A retail device used to sell fare products.

    Can be used to record fulfilment.

    :ivar id: Identifier of RETAIL DEVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
