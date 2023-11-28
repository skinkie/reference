from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.coupling_type_enumeration import CouplingTypeEnumeration
from netex.current_type_enumeration import CurrentTypeEnumeration
from netex.plug_type_enumeration import PlugTypeEnumeration
from netex.type_of_plug_ref import TypeOfPlugRef
from netex.vehicle_equipment_profile_version_structure import VehicleEquipmentProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingEquipmentProfileVersionStructure(VehicleEquipmentProfileVersionStructure):
    """
    Type for a CHARGING EQUIPMENT PROFILE.

    :ivar coupling_type: Type of coupling. See allowed values.
    :ivar plug_type: Type of Plug. See allowed values.
    :ivar type_of_plug_ref:
    :ivar current_type: Type of current. See allowed values.
    :ivar charging_voltage: CHarging voltage in Volts.
    :ivar maximum_charging_power: Maximum charging power in Watts,
        available, determining how long charging willtake
    :ivar preparation_duration: Normal period need to set up charging.
    :ivar finalisation_duration: Normal time to decouple after charging.
    """
    class Meta:
        name = "ChargingEquipmentProfile_VersionStructure"

    coupling_type: Optional[CouplingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CouplingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    plug_type: Optional[PlugTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PlugType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_plug_ref: Optional[TypeOfPlugRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPlugRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    current_type: Optional[CurrentTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CurrentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ChargingVoltage",
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
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    finalisation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinalisationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
