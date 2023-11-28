from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.authority_ref import AuthorityRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.management_agent_ref import ManagementAgentRef
from netex.multilingual_string import MultilingualString
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.security_listings_rel_structure import SecurityListingsRelStructure
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.travel_agent_ref import TravelAgentRef
from netex.type_of_security_list_ref import TypeOfSecurityListRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SecurityListVersionStructure(DataManagedObjectStructure):
    """Type for SECURITY LIST.

    +v1.1

    :ivar name: Name of SECURITY LIST.
    :ivar description: Description of SECURITY LIST.
    :ivar type_of_security_list_ref:
    :ivar choice:
    :ivar security_listings: Items in SECURITY LIST.
    """
    class Meta:
        name = "SecurityList_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    type_of_security_list_ref: Optional[TypeOfSecurityListRef] = field(
        default=None,
        metadata={
            "name": "TypeOfSecurityListRef",
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
    security_listings: Optional[SecurityListingsRelStructure] = field(
        default=None,
        metadata={
            "name": "securityListings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
