from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union

from .facility_ref import FacilityRef
from .facility_structure import FacilityStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .passenger_capacity_structure import PassengerCapacityStructure
from .train_in_compound_train import TrainInCompoundTrain
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .type_of_fuel_enumeration import TypeOfFuelEnumeration
from .vehicle_feature import VehicleFeature

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CompoundTrainStructure:
    compound_train_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompoundTrainCode",
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
    maximum_passenger_capacities: Optional["CompoundTrainStructure.MaximumPassengerCapacities"] = field(
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
    facilities: Optional["CompoundTrainStructure.Facilities"] = field(
        default=None,
        metadata={
            "name": "Facilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    trains_in_compound_train: Optional["CompoundTrainStructure.TrainsInCompoundTrain"] = field(
        default=None,
        metadata={
            "name": "TrainsInCompoundTrain",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class TrainsInCompoundTrain:
        train_in_compound_train_ref_or_train_in_compound_train: List[Union[TrainInCompoundTrainRef, TrainInCompoundTrain]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "TrainInCompoundTrainRef",
                        "type": TrainInCompoundTrainRef,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "TrainInCompoundTrain",
                        "type": TrainInCompoundTrain,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
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
