from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.authority_ref import AuthorityRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.management_agent_ref import ManagementAgentRef
from netex.multilingual_string import MultilingualString
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.organisation_role_enumeration import OrganisationRoleEnumeration
from netex.other_organisation_ref import OtherOrganisationRef
from netex.responsibility_role_ref import ResponsibilityRoleRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RelatedOrganisationVersionStructure(VersionedChildStructure):
    """
    Type for an RELATED ORGANISATION.

    :ivar name: Name of RELATED ORGANISATION.
    :ivar description: Description of the nature pf the  Relationship.
    :ivar choice:
    :ivar organisation_role_type: Role of the related Organbisation
    :ivar responsibility_role_ref:
    """
    class Meta:
        name = "RelatedOrganisation_VersionStructure"

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
    organisation_role_type: Optional[OrganisationRoleEnumeration] = field(
        default=None,
        metadata={
            "name": "OrganisationRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_role_ref: Optional[ResponsibilityRoleRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
