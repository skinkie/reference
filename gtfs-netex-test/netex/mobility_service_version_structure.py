from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from netex.authority_ref import AuthorityRef
from netex.equipment_version_structure import EquipmentVersionStructure
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.management_agent_ref import ManagementAgentRef
from netex.multilingual_string import MultilingualString
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.service_booking_arrangements_structure import ServiceBookingArrangementsStructure
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.topographic_place_ref import TopographicPlaceRef
from netex.travel_agent_ref import TravelAgentRef
from netex.type_of_mobility_service_ref import TypeOfMobilityServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceVersionStructure(EquipmentVersionStructure):
    """
    Type for a MOBILITY SERVICE.

    :ivar short_name: Short Name for service
    :ivar start_date: Start date from when services are available
    :ivar type_of_mobility_service_ref:
    :ivar choice:
    :ivar topographic_place_ref:
    :ivar service_booking_arrangements: Booking Arrangements for
        service.
    """
    class Meta:
        name = "MobilityService_VersionStructure"

    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_mobility_service_ref: Optional[TypeOfMobilityServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfMobilityServiceRef",
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
            ),
        }
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_booking_arrangements: Optional[ServiceBookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "ServiceBookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
