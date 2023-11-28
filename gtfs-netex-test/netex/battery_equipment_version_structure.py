from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.place_equipment_version_structure import PlaceEquipmentVersionStructure
from netex.type_of_battery_chemistry_ref import TypeOfBatteryChemistryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BatteryEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    """
    Type for a BATTERY EQUIPMENT.

    :ivar battery_capacity: Battery capacity stated by the manufacturer
        in Watt Hours [Wh]
    :ivar battery_usable_capacity: Usable battery capacity stated in
        Watt Hours [Wh]
    :ivar nominal_voltage: Voltage for battery in volts.
    :ivar maximum_charging_power: Maximum charging power of the grid
        supply [W]. The sum of the current  power of all connected
        charging points cannot exceed this value.
    :ivar type_of_battery_chemistry_ref:
    """
    class Meta:
        name = "BatteryEquipment_VersionStructure"

    battery_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BatteryCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    battery_usable_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BatteryUsableCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    nominal_voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NominalVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_charging_power: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumChargingPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_battery_chemistry_ref: Optional[TypeOfBatteryChemistryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfBatteryChemistryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
