from dataclasses import dataclass
from netex.medium_access_device_version_structure import MediumAccessDeviceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EmvCardVersionStructure(MediumAccessDeviceVersionStructure):
    """
    Type for EMV CARD restricts id.
    """
    class Meta:
        name = "EmvCard_VersionStructure"
