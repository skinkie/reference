from dataclasses import dataclass, field
from typing import Optional
from netex.air_submode_enumeration import AirSubmodeEnumeration
from netex.bus_submode_enumeration import BusSubmodeEnumeration
from netex.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.rail_submode_enumeration import RailSubmodeEnumeration
from netex.self_drive_submode_enumeration import SelfDriveSubmodeEnumeration
from netex.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.taxi_submode_enumeration import TaxiSubmodeEnumeration
from netex.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.tram_submode_enumeration import TramSubmodeEnumeration
from netex.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllSubmodeStructure:
    """
    Type for all Sub modes.
    """
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FunicularSubmode",
                    "type": FunicularSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SnowAndIceSubmode",
                    "type": SnowAndIceSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiSubmode",
                    "type": TaxiSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SelfDriveSubmode",
                    "type": SelfDriveSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
