from dataclasses import dataclass, field
from typing import List, Optional, Union

from .affected_network_structure import AffectedNetworkStructure
from .affected_operator_structure import AffectedOperatorStructure
from .affected_place_structure import AffectedPlaceStructure
from .affected_roads_structure import AffectedRoadsStructure
from .affected_stop_point_structure import (
    AffectedStopPlaceStructure,
    AffectedStopPointStructure,
)
from .affected_vehicle_journey_structure import AffectedVehicleJourneyStructure
from .affected_vehicle_structure import AffectedVehicleStructure
from .area_of_interest_enum import AreaOfInterestEnum
from .empty_type import EmptyType
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectsScopeStructure:
    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "AreaOfInterest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operators: Optional["AffectsScopeStructure.Operators"] = field(
        default=None,
        metadata={
            "name": "Operators",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    networks: Optional["AffectsScopeStructure.Networks"] = field(
        default=None,
        metadata={
            "name": "Networks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points: Optional["AffectsScopeStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_places: Optional["AffectsScopeStructure.StopPlaces"] = field(
        default=None,
        metadata={
            "name": "StopPlaces",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    places: Optional["AffectsScopeStructure.Places"] = field(
        default=None,
        metadata={
            "name": "Places",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journeys: Optional["AffectsScopeStructure.VehicleJourneys"] = field(
        default=None,
        metadata={
            "name": "VehicleJourneys",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicles: Optional["AffectsScopeStructure.Vehicles"] = field(
        default=None,
        metadata={
            "name": "Vehicles",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    roads: Optional[AffectedRoadsStructure] = field(
        default=None,
        metadata={
            "name": "Roads",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class Operators:
        all_operators_or_affected_operator: List[Union[EmptyType, AffectedOperatorStructure]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "AllOperators",
                        "type": EmptyType,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "AffectedOperator",
                        "type": AffectedOperatorStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class Networks:
        affected_network: List[AffectedNetworkStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedNetwork",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class StopPoints:
        affected_stop_point: List[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class StopPlaces:
        affected_stop_place: List[AffectedStopPlaceStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Places:
        affected_place: List[AffectedPlaceStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class VehicleJourneys:
        affected_vehicle_journey: List[AffectedVehicleJourneyStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedVehicleJourney",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Vehicles:
        affected_vehicle: List[AffectedVehicleStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedVehicle",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
