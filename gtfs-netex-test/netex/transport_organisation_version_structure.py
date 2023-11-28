from dataclasses import dataclass, field
from typing import List, Optional
from netex.air_submode_enumeration import AirSubmodeEnumeration
from netex.all_modes_enumeration import AllModesEnumeration
from netex.bus_submode_enumeration import BusSubmodeEnumeration
from netex.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.contact_structure import ContactStructure
from netex.country_ref import CountryRef
from netex.departments_rel_structure import DepartmentsRelStructure
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.mode_refs_rel_structure import ModeRefsRelStructure
from netex.operator_activities_enumeration import OperatorActivitiesEnumeration
from netex.organisation_version_structure import OrganisationVersionStructure
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.postal_address import PostalAddress
from netex.postal_address_version_structure import PostalAddressVersionStructure
from netex.rail_submode_enumeration import RailSubmodeEnumeration
from netex.road_address import RoadAddress
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.self_drive_submode_enumeration import SelfDriveSubmodeEnumeration
from netex.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.taxi_submode_enumeration import TaxiSubmodeEnumeration
from netex.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.tram_submode_enumeration import TramSubmodeEnumeration
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef
from netex.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportOrganisationVersionStructure(OrganisationVersionStructure):
    """
    Type for an TRANSPORT ORGANISATION.

    :ivar country_ref:
    :ivar postal_address_or_road_address_or_address:
    :ivar primary_mode: Primary transport MODE of TRANSPORT ORGANISATION
    :ivar choice:
    :ivar choice_1:
    :ivar operator_activities: Activities undertaken by OPERATOR.
    :ivar customer_service_contact_details: Contact details for Customer
        service use.
    :ivar departments: Departments of OPERATOR.
    :ivar other_modes: Additional transport MODEs for OPERATOR.
    """
    class Meta:
        name = "TransportOrganisation_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address_or_road_address_or_address: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Address",
                    "type": PostalAddressVersionStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    primary_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "PrimaryMode",
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
    operator_activities: List[OperatorActivitiesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OperatorActivities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    customer_service_contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "CustomerServiceContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departments: Optional[DepartmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_modes: Optional[ModeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "otherModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
