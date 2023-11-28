from dataclasses import dataclass, field
from typing import Optional
from netex.air_submode_enumeration import AirSubmodeEnumeration
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.bus_submode_enumeration import BusSubmodeEnumeration
from netex.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.polygon import Polygon
from netex.rail_submode_enumeration import RailSubmodeEnumeration
from netex.simple_point_version_structure import SimplePointVersionStructure
from netex.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.stop_place_refs_rel_structure import StopPlaceRefsRelStructure
from netex.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.tram_submode_enumeration import TramSubmodeEnumeration
from netex.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfStopPlacesStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP of STOP PLACEs.

    :ivar public_code:
    :ivar members: Stations and stops in GROUP of STOP PLACEs.
    :ivar alternative_names: Alternative names for the GROUP of STOP
        PLACEs.
    :ivar centroid: Centre Coordinates of GROUP of STOP PLACEs.
    :ivar polygon:
    :ivar transport_mode: Primary MODE of Vehicle transport associated
        by this component.
    :ivar choice:
    """
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[StopPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    centroid: Optional[SimplePointVersionStructure] = field(
        default=None,
        metadata={
            "name": "Centroid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
            ),
        }
    )
