from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .installed_equipment_version_structure import InstalledEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "SpotEquipment_VersionStructure"

    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_from_floor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightFromFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_power_supply: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasPowerSupply",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_usb_power_socket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasUsbPowerSocket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
