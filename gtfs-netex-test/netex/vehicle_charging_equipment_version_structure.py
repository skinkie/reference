from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleChargingEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    """
    Type for a VEHICLE CHARGING EQUIPMENT.

    :ivar free_recharging: whether shelter is enclosed.
    :ivar reservation_required: Whether reservation is required.
    :ivar reservation_url: Type of storage.
    :ivar maximum_power: Maximum charging power of the grid supply [W].
        The sum of the current power of all connected charging points
        cannot exceed this value.
    :ivar grid_voltage: Grid Voltage to the equipment.
    """
    class Meta:
        name = "VehicleChargingEquipment_VersionStructure"

    free_recharging: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeRecharging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reservation_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reservation_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_power: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    grid_voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GridVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
