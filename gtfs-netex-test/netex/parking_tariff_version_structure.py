from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.authority_ref import AuthorityRef
from netex.cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.group_of_operators_ref import GroupOfOperatorsRef
from netex.info_links_rel_structure import InfoLinksRelStructure
from netex.management_agent_ref import ManagementAgentRef
from netex.multilingual_string import MultilingualString
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.parking_charge_bands_rel_structure import ParkingChargeBandsRelStructure
from netex.parking_refs_rel_structure import ParkingRefsRelStructure
from netex.parking_stay_enumeration import ParkingStayEnumeration
from netex.parking_user_enumeration import ParkingUserEnumeration
from netex.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.price_unit_ref import PriceUnitRef
from netex.quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from netex.time_unit_ref import TimeUnitRef
from netex.transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from netex.travel_agent_ref import TravelAgentRef
from netex.type_of_tariff_ref import TypeOfTariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingTariffVersionStructure(DataManagedObjectStructure):
    """
    Type for a PARKING TARIFF.

    :ivar name: Name of TARIFF.
    :ivar alternative_names: ATERNATIVE NAMEs for TARIFF.
    :ivar description: Description of TARIFF.
    :ivar notice_assignments: NOTICE explaining TARIFF.
    :ivar document_links: Timetable documents associated with the Tariff
        e.g pdf files +v1.1
    :ivar choice:
    :ivar time_unit_ref:
    :ivar time_intervals: VALIDITY PARAMETER ASSIGNMENTs making up
        TARIFF.
    :ivar time_structure_factors: TIME STRUCTURE FACTORs making up
        TARIFF.
    :ivar quality_structure_factors: QUALITY STRUCTURE ELEMENTs making
        up TARIFF.
    :ivar parking_user_type: Type of users: disabled, all etc.
    :ivar parking_stay_type: Nature of stay allowed in PARKING.
    :ivar parking_vehicle_types: Type of Vehicle for which PARKING
        TARIFF applies.  Fixed values.
    :ivar vehicle_types: Opnen specifcation of VEHICLE TYPEs + v1.1
    :ivar applies_to: PaARKIMNGs to which this tariff applies
    :ivar type_of_tariff_ref:
    :ivar additional_tax: Whether additional tax is charged.
    :ivar parking_charge_bands: Charge bands for parking.
    :ivar price_unit_ref:
    :ivar price_groups: QUALITY STRUCTURE ELEMENTs making up TARIFF.
    :ivar fare_tables: QUALITY STRUCTURE ELEMENTs making up TARIFF.
    """
    class Meta:
        name = "ParkingTariff_VersionStructure"

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
    parking_user_type: Optional[ParkingUserEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingUserType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_stay_type: Optional[ParkingStayEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingStayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_vehicle_types: List[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    vehicle_types: Optional[TransportTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    applies_to: Optional[ParkingRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "appliesTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    additional_tax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdditionalTax",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_charge_bands: Optional[ParkingChargeBandsRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingChargeBands",
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
