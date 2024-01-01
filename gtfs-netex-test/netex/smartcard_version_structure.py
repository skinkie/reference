from dataclasses import dataclass
from .medium_access_device_version_structure import (
    MediumAccessDeviceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SmartcardVersionStructure(MediumAccessDeviceVersionStructure):
    class Meta:
        name = "Smartcard_VersionStructure"
