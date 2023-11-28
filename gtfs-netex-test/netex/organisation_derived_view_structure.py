from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.authority_ref import AuthorityRef
from netex.contact_structure import ContactStructure
from netex.derived_view_structure import DerivedViewStructure
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.management_agent_ref import ManagementAgentRef
from netex.multilingual_string import MultilingualString
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationDerivedViewStructure(DerivedViewStructure):
    """
    Type for an ORGANISATION VIEW.

    :ivar choice:
    :ivar name: The name of the ORGANISATION.
    :ivar short_name: A short name of the ORGANISATION.
    :ivar legal_name: The legal name of the ORGANISATION, if different
        from Name.
    :ivar trading_name: The Trading name of the ORGANISATION given to
        the Public - If different from Name or Legal Name.
    :ivar alternative_names: Alternativie names for ORGANISATION.
    :ivar contact_details: Contact details for ORGANISATION for Public
        use.
    """
    class Meta:
        name = "Organisation_DerivedViewStructure"

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
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    legal_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "LegalName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trading_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "TradingName",
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
    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
