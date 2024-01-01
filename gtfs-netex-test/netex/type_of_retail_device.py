from dataclasses import dataclass
from .type_of_retail_device_version_structure import (
    TypeOfRetailDeviceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRetailDevice(TypeOfRetailDeviceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
