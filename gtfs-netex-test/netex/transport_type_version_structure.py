from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef, Optional, Union

from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .deck_plan_ref import DeckPlanRef
from .entity_in_version_structure import DataManagedObjectStructure
from .fuel_type_enumeration import FuelTypeEnumeration
from .multilingual_string import MultilingualString
from .passenger_capacity_structure import PassengerCapacityStructure
from .private_code import PrivateCode
from .propulsion_type_enumeration import PropulsionTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TransportTypeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TransportType_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    euro_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reversing_direction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    self_propelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    propulsion_type: list[PropulsionTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PropulsionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    fuel_type_or_type_of_fuel: Optional[Union["TransportTypeVersionStructure.FuelType", "TransportTypeVersionStructure.TypeOfFuel"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FuelType",
                    "type": ForwardRef("TransportTypeVersionStructure.FuelType"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFuel",
                    "type": ForwardRef("TransportTypeVersionStructure.TypeOfFuel"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    maximum_range: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_velocity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumVelocity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_capacity: Optional[PassengerCapacityStructure] = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_plan_ref: Optional[DeckPlanRef] = field(
        default=None,
        metadata={
            "name": "DeckPlanRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(slots=True, kw_only=True)
    class FuelType:
        value: list[FuelTypeEnumeration] = field(
            default_factory=list,
            metadata={
                "tokens": True,
            },
        )

    @dataclass(slots=True, kw_only=True)
    class TypeOfFuel:
        value: FuelTypeEnumeration = field(
            metadata={
                "required": True,
            }
        )
