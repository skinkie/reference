from dataclasses import dataclass, field
from typing import Optional, Union

from .administrative_zones_rel_structure import AdministrativeZonesRelStructure
from .authority_ref import AuthorityRef
from .contact_structure import ContactStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .general_organisation_ref import GeneralOrganisationRef
from .location_structure_2 import LocationStructure2
from .management_agent_ref import ManagementAgentRef
from .multilingual_string import MultilingualString
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .organisation_refs_rel_structure import OrganisationRefsRelStructure
from .other_organisation_ref import OtherOrganisationRef
from .private_code import PrivateCode
from .public_code_structure import PublicCodeStructure
from .responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .type_of_organisation_part_ref import TypeOfOrganisationPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OrganisationPartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OrganisationPart_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[PublicCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisation_ref_or_other_organisation_ref_or_transport_organisation_ref: Optional[Union[RetailConsortiumRef, OnlineServiceOperatorRef, GeneralOrganisationRef, ManagementAgentRef, ServicedOrganisationRef, TravelAgentRef, OtherOrganisationRef, AuthorityRef, OperatorRef, OrganisationRef]] = field(
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
        },
    )
    type_of_organisation_part_ref: Optional[TypeOfOrganisationPartRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    administrative_zones: Optional[AdministrativeZonesRelStructure] = field(
        default=None,
        metadata={
            "name": "administrativeZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    own_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "ownResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delegated_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delegated_from: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
