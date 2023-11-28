from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.fuel_type_enumeration import FuelTypeEnumeration
from netex.multilingual_string import MultilingualString
from netex.passenger_capacity_structure import PassengerCapacityStructure
from netex.private_code import PrivateCode
from netex.propulsion_type_enumeration import PropulsionTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportTypeVersionStructure(DataManagedObjectStructure):
    """
    Type for a TRANSPORT TYPE.

    :ivar name: Name of TRANSPORT TYPE.
    :ivar short_name: Short Name of TRANSPORT TYPE.
    :ivar description: Description of TRANSPORT TYPE.
    :ivar private_code:
    :ivar euro_class: Euroclass of the vehicle type.
    :ivar reversing_direction: Whether vehicles of the type have a
        reversing direction.
    :ivar self_propelled: Whether vehicles of the type are self-
        propelled.
    :ivar propulsion_type: Type of power used +v1.2.2
    :ivar fuel_type_or_type_of_fuel:
    :ivar maximum_range: Maximum range between refuelling. +v1.2.2
    :ivar transport_mode: MODE of Vehicle transport associated with
        VEHICLE TYPE. +v1.2.2
    :ivar passenger_capacity: Total Number of passengers that VEHICLE
        TYPE can carry.
    """
    class Meta:
        name = "TransportType_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    euro_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reversing_direction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    self_propelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    propulsion_type: Optional[PropulsionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PropulsionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fuel_type_or_type_of_fuel: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FuelType",
                    "type": FuelTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFuel",
                    "type": FuelTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    maximum_range: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_capacity: Optional[PassengerCapacityStructure] = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
