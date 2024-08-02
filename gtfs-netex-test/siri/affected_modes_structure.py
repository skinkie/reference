from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .access_modes_enumeration import AccessModesEnumeration
from .air_submode import AirSubmode
from .bus_submode import BusSubmode
from .coach_submode import CoachSubmode
from .empty_type import EmptyType
from .metro_submode import MetroSubmode
from .rail_submode import RailSubmode
from .telecabin_submode import TelecabinSubmode
from .tram_submode import TramSubmode
from .vehicle_mode import VehicleMode
from .water_submode import WaterSubmode

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedModesStructure:
    all_modes_or_mode: List[Union[EmptyType, "AffectedModesStructure.Mode"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllModes",
                    "type": EmptyType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Mode",
                    "type": ForwardRef("AffectedModesStructure.Mode"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Mode:
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
