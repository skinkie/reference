from dataclasses import dataclass, field
from netex.smartcard_version_structure import SmartcardVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Smartcard(SmartcardVersionStructure):
    """A  smart card with the necessary facilities (hardware and software) are) to
    host a  MEDIUM APPLICATION INSTANCE and communicate with a control device.

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
