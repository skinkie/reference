from dataclasses import dataclass, field
from typing import List, Optional
from netex.air_submode_enumeration import AirSubmodeEnumeration
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.bus_submode_enumeration import BusSubmodeEnumeration
from netex.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.rail_submode_enumeration import RailSubmodeEnumeration
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.site_component_version_structure import SiteComponentVersionStructure
from netex.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.tram_submode_enumeration import TramSubmodeEnumeration
from netex.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef
from netex.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceComponentVersionStructure(SiteComponentVersionStructure):
    """
    Type for a STOP PLACE COMPONENT.

    :ivar transport_mode: Primary MODE of Vehicle transport associated
        by this component.
    :ivar choice:
    :ivar choice_1:
    :ivar other_transport_modes: Public transport MODES which may be
        accessed through associated place.
    :ivar tariff_zones: TARIFF ZONEs into which component falls.
    """
    class Meta:
        name = "StopPlaceComponent_VersionStructure"

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
    choice_1: Optional[object] = field(
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
