from dataclasses import dataclass

from .medium_access_device_ref_structure import MediumAccessDeviceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EmvCardRefStructure(MediumAccessDeviceRefStructure):
    pass
