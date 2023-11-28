from dataclasses import dataclass, field
from typing import List, Optional
from netex.access_spaces_rel_structure import AccessSpacesRelStructure
from netex.accesses_rel_structure import AccessesRelStructure
from netex.air_submode_enumeration import AirSubmodeEnumeration
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.bus_submode_enumeration import BusSubmodeEnumeration
from netex.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.explicit_equipments_rel_structure import ExplicitEquipmentsRelStructure
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.interchange_weighting_enumeration import InterchangeWeightingEnumeration
from netex.limited_use_type_enumeration import LimitedUseTypeEnumeration
from netex.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.navigation_paths_rel_structure import NavigationPathsRelStructure
from netex.path_junctions_rel_structure import PathJunctionsRelStructure
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.quays_rel_structure import QuaysRelStructure
from netex.rail_submode_enumeration import RailSubmodeEnumeration
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.site_path_links_rel_structure import SitePathLinksRelStructure
from netex.site_version_structure import SiteVersionStructure
from netex.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.stop_place_weight_enumeration import StopPlaceWeightEnumeration
from netex.stop_type_enumeration import StopTypeEnumeration
from netex.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure
from netex.tram_submode_enumeration import TramSubmodeEnumeration
from netex.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef
from netex.vehicle_stopping_places_rel_structure import VehicleStoppingPlacesRelStructure
from netex.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceVersionStructure(SiteVersionStructure):
    """
    Type for a Version of a STOP PLACE.

    :ivar public_code: Short public code for passengers to use when
        uniquely identifying the stop by SMS and other self-service
        channels.
    :ivar transport_mode: Primary MODE of Vehicle transport associated
        by this component.
    :ivar choice_1:
    :ivar choice_2:
    :ivar other_transport_modes: Public transport MODES which may be
        accessed through associated place.
    :ivar tariff_zones: TARIFF ZONEs into which component falls.
    :ivar stop_place_type: Type of STOP PLACE.
    :ivar border_crossing: Whether STOP PLACE is a border crossing, that
        is a point, at which an international boundary between two
        countries may be crossed.
    :ivar unlocalised_equipments: Items of EQUIPMENT associated with
        STOP PLACE but not assigned to a point within it. More Localized
        EQUIPMENT should be included in an EQUIPMENT place.
    :ivar served_places: TOPOGRAPHICAL PLACEs that the STOP PLACE
        serves.
    :ivar main_terminus_for_places: TOPOGRAPHICAL PLACEs for which the
        STOP PLACE is a main terminus. Only certain stations will be
        deemed the main STOP PLACEs points. For example London has many
        rail stations but only some are main line terminii. Geographic
        containment is not necessarily implied For example London
        Gatwick and, London Stansted airports are not in London, but are
        designated airports for London. Norwich station is not in
        Norwich, etc.
    :ivar limited_use: Further categorisation of stop as having
        topographic limitations.
    :ivar weighting: Default rating of the STOP PLACE for making
        interchanges.
    :ivar stop_place_weight: Type of expected INTERCHANGE at a STOP
        PLACE for use in journey planners and also for possible legal
        classification. +v1.1
    :ivar quays: QUAYs within the STOP PLACE.
    :ivar access_spaces: ACCESS SPACEs within the STOP PLACE.
    :ivar path_links: PATH LINKs for SITE.
    :ivar path_junctions: PATH JUNCTIONs within the SITE and or between
        the SITE elsewhere.
    :ivar accesses: ACCESS links for SITE.
    :ivar navigation_paths: NAVIGATION PATHs within the SITE and or
        between the SITE elsewhere.
    :ivar vehicle_stopping_places: VEHICLE STOPPING PLACEs within STOP
        PLACE.
    """
    class Meta:
        name = "StopPlace_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
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
    choice_1: Optional[object] = field(
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
    choice_2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    other_transport_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OtherTransportModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    tariff_zones: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_type: Optional[StopTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_crossing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BorderCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    unlocalised_equipments: Optional[ExplicitEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "unlocalisedEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    served_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "servedPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    main_terminus_for_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "mainTerminusForPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limited_use: Optional[LimitedUseTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    weighting: Optional[InterchangeWeightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Weighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_weight: Optional[StopPlaceWeightEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quays: Optional[QuaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_spaces: Optional[AccessSpacesRelStructure] = field(
        default=None,
        metadata={
            "name": "accessSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_links: Optional[SitePathLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junctions: Optional[PathJunctionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accesses: Optional[AccessesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_places: Optional[VehicleStoppingPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleStoppingPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
