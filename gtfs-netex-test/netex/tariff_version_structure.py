from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.assistance_service_ref import AssistanceServiceRef
from netex.authority_ref import AuthorityRef
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.catering_service_ref import CateringServiceRef
from netex.cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.communication_service_ref import CommunicationServiceRef
from netex.complaints_service_ref import ComplaintsServiceRef
from netex.customer_service_ref import CustomerServiceRef
from netex.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.fare_structure_elements_rel_structure import FareStructureElementsRelStructure
from netex.flexible_line_ref import FlexibleLineRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from netex.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.geographical_unit_ref import GeographicalUnitRef
from netex.group_of_lines_ref import GroupOfLinesRef
from netex.group_of_operators_ref import GroupOfOperatorsRef
from netex.groups_of_distance_matrix_elements_rel_structure import GroupsOfDistanceMatrixElementsRelStructure
from netex.hire_service_ref import HireServiceRef
from netex.info_links_rel_structure import InfoLinksRelStructure
from netex.left_luggage_service_ref import LeftLuggageServiceRef
from netex.line_ref import LineRef
from netex.local_service_ref import LocalServiceRef
from netex.lost_property_service_ref import LostPropertyServiceRef
from netex.luggage_service_ref import LuggageServiceRef
from netex.management_agent_ref import ManagementAgentRef
from netex.meeting_point_service_ref import MeetingPointServiceRef
from netex.money_service_ref import MoneyServiceRef
from netex.multilingual_string import MultilingualString
from netex.network_ref import NetworkRef
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.online_service_ref import OnlineServiceRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.price_unit_ref import PriceUnitRef
from netex.private_code import PrivateCode
from netex.quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.retail_service_ref import RetailServiceRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.tariff_basis_enumeration import TariffBasisEnumeration
from netex.taxi_service_ref import TaxiServiceRef
from netex.ticketing_service_ref import TicketingServiceRef
from netex.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from netex.time_unit_ref import TimeUnitRef
from netex.travel_agent_ref import TravelAgentRef
from netex.type_of_tariff_ref import TypeOfTariffRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TariffVersionStructure(DataManagedObjectStructure):
    """
    Type for TARIFF.

    :ivar name: Name of TARIFF.
    :ivar alternative_names: ATERNATIVE NAMEs for TARIFF.
    :ivar description: Description of TARIFF.
    :ivar notice_assignments: NOTICE explaining TARIFF.
    :ivar document_links: Timetable documents associated with the Tariff
        e.g pdf files +v1.1
    :ivar private_code:
    :ivar choice:
    :ivar choice_1:
    :ivar choice_2:
    :ivar type_of_tariff_ref:
    :ivar tariff_basis: Classification of  Tariff Butasis. Defaut is
        Route (Tap TSI)
    :ivar return_fare_twice_single: Whether return fare is  normally
        twice single fare. Default is true.
    :ivar geographical_unit_ref:
    :ivar geographical_intervals: GEOGRAPHICAL INTERVALs  making up
        TARIFF.
    :ivar geographical_structure_factors: GEOGRAPHICAL STRUCTURE FACTORs
        making up TARIFF.
    :ivar time_unit_ref:
    :ivar time_intervals: VALIDITY PARAMETER ASSIGNMENTs making up
        TARIFF.
    :ivar time_structure_factors: TIME STRUCTURE FACTORs making up
        TARIFF.
    :ivar quality_structure_factors: QUALITY STRUCTURE ELEMENTs making
        up TARIFF.
    :ivar fare_structure_elements: FARE STRUCTURE ELEMENTs making up
        TARIFF.
    :ivar distance_matrix_elements: DISTANCE MATRIX ELEMENTs making up
        TARIFF.
    :ivar groups_of_distance_matrix_elements: GROUPs of DISTANCE MATRIX
        ELEMENTs making up TARIFF.
    :ivar price_unit_ref:
    :ivar price_groups: QUALITY STRUCTURE ELEMENTs making up TARIFF.
    :ivar fare_tables: QUALITY STRUCTURE ELEMENTs making up TARIFF.
    """
    class Meta:
        name = "Tariff_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
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
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceOperatorRef",
                    "type": OnlineServiceOperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
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
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
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
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringServiceRef",
                    "type": CateringServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailServiceRef",
                    "type": RetailServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyServiceRef",
                    "type": MoneyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireServiceRef",
                    "type": HireServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationServiceRef",
                    "type": CommunicationServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointServiceRef",
                    "type": MeetingPointServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageServiceRef",
                    "type": LeftLuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageServiceRef",
                    "type": LuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyServiceRef",
                    "type": LostPropertyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsServiceRef",
                    "type": ComplaintsServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerServiceRef",
                    "type": CustomerServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceServiceRef",
                    "type": AssistanceServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingServiceRef",
                    "type": TicketingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LocalServiceRef",
                    "type": LocalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    type_of_tariff_ref: Optional[TypeOfTariffRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_basis: Optional[TariffBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    return_fare_twice_single: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnFareTwiceSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_intervals: Optional[GeographicalIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factors: Optional[GeographicalStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_intervals: Optional[TimeIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factors: Optional[QualityStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "qualityStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_elements: Optional[FareStructureElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareStructureElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_elements: Optional[DistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "distanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_distance_matrix_elements: Optional[GroupsOfDistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
