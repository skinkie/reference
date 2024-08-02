from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from .facility_ref import FacilityRef
from .facility_structure import FacilityStructure
from .fare_classes import FareClasses
from .natural_language_string_structure import NaturalLanguageStringStructure
from .passenger_capacity_structure import PassengerCapacityStructure
from .train_element_type_enumeration import TrainElementTypeEnumeration
from .type_of_fuel_enumeration import TypeOfFuelEnumeration
from .vehicle_feature import VehicleFeature

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainElementStructure:
    train_element_code: str = field(
        metadata={
            "name": "TrainElementCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    train_element_type: Optional[TrainElementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainElementType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    fare_classes: Optional[FareClasses] = field(
        default=None,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    short_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    private_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reversing_direction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    self_propelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    type_of_fuel: Optional[TypeOfFuelEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfFuel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    euro_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_passenger_capacities: Optional["TrainElementStructure.MaximumPassengerCapacities"] = field(
        default=None,
        metadata={
            "name": "MaximumPassengerCapacities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    has_hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facilities: Optional["TrainElementStructure.Facilities"] = field(
        default=None,
        metadata={
            "name": "Facilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class MaximumPassengerCapacities:
        maximum_passenger_capacity: List[PassengerCapacityStructure] = field(
            default_factory=list,
            metadata={
                "name": "MaximumPassengerCapacity",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Facilities:
        vehicle_feature_or_facility_or_facility_ref: List[Union[VehicleFeature, FacilityStructure, FacilityRef]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "VehicleFeature",
                        "type": VehicleFeature,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "Facility",
                        "type": FacilityStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "FacilityRef",
                        "type": FacilityRef,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
