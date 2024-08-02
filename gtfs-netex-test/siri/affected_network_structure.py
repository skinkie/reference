from dataclasses import dataclass, field
from typing import List, Optional, Union

from .access_modes_enumeration import AccessModesEnumeration
from .affected_operator_structure import AffectedOperatorStructure
from .affected_section_structure import AffectedSectionStructure
from .affected_stop_point_structure import (
    AffectedLineStructure,
    AffectedRouteStructure,
)
from .air_submode import AirSubmode
from .bus_submode import BusSubmode
from .coach_submode import CoachSubmode
from .empty_type import EmptyType
from .extensions_1 import Extensions1
from .metro_submode import MetroSubmode
from .natural_language_string_structure import NaturalLanguageStringStructure
from .network_ref_structure import NetworkRefStructure
from .rail_submode import RailSubmode
from .telecabin_submode import TelecabinSubmode
from .tram_submode import TramSubmode
from .vehicle_mode import VehicleMode
from .water_submode import WaterSubmode

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedNetworkStructure:
    affected_operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_ref: Optional[NetworkRefStructure] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "NetworkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    routes_affected: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "RoutesAffected",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    air_submode_or_bus_submode_or_coach_submode_or_metro_submode_or_rail_submode_or_tram_submode_or_water_submode_or_telecabin_submode: Optional[Union[AirSubmode, BusSubmode, CoachSubmode, MetroSubmode, RailSubmode, TramSubmode, WaterSubmode, TelecabinSubmode]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    access_mode: Optional[AccessModesEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_lines_or_selected_routes_or_affected_section_or_affected_line: List[Union[EmptyType, AffectedRouteStructure, AffectedSectionStructure, AffectedLineStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllLines",
                    "type": EmptyType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SelectedRoutes",
                    "type": AffectedRouteStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AffectedSection",
                    "type": AffectedSectionStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AffectedLine",
                    "type": AffectedLineStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
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
