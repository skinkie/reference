from dataclasses import dataclass, field
from typing import Optional, Union

from .air_submode import AirSubmode
from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .bus_submode import BusSubmode
from .coach_submode import CoachSubmode
from .funicular_submode import FunicularSubmode
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .metro_submode import MetroSubmode
from .polygon import Polygon
from .public_code_structure import PublicCodeStructure
from .rail_submode import RailSubmode
from .simple_point_version_structure import SimplePointVersionStructure
from .snow_and_ice_submode import SnowAndIceSubmode
from .stop_place_refs_rel_structure import StopPlaceRefsRelStructure
from .telecabin_submode import TelecabinSubmode
from .tram_submode import TramSubmode
from .water_submode import WaterSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfStopPlacesStructure(GroupOfEntitiesVersionStructure):
    public_code: Optional[PublicCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[StopPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    centroid: Optional[SimplePointVersionStructure] = field(
        default=None,
        metadata={
            "name": "Centroid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    air_submode_or_bus_submode_or_coach_submode_or_funicular_submode_or_metro_submode_or_tram_submode_or_telecabin_submode_or_rail_submode_or_water_submode_or_snow_and_ice_submode: Optional[
        Union[AirSubmode, BusSubmode, CoachSubmode, FunicularSubmode, MetroSubmode, TramSubmode, TelecabinSubmode, RailSubmode, WaterSubmode, SnowAndIceSubmode]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FunicularSubmode",
                    "type": FunicularSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SnowAndIceSubmode",
                    "type": SnowAndIceSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
