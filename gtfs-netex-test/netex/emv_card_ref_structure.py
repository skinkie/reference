from dataclasses import dataclass
from .medium_access_device_ref_structure import MediumAccessDeviceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EmvCardRefStructure(MediumAccessDeviceRefStructure):
    value: RestrictedVar
