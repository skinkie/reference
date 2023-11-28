from dataclasses import dataclass, field
from netex.mobile_device_version_structure import MobileDeviceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobileDevice(MobileDeviceVersionStructure):
    """A mobile device (mobile phone, tablet, etc) with the necessary facilities
    (hardware and software) to host a MEDIUM APPLICATION INSTANCE and communicate
    with a control device.

    +v1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
