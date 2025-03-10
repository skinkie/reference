from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .authority_ref import AuthorityRef
from .general_organisation_ref import GeneralOrganisationRef
from .journey_accounting_enumeration import JourneyAccountingEnumeration
from .management_agent_ref import ManagementAgentRef
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .supply_contract_ref import SupplyContractRef
from .travel_agent_ref import TravelAgentRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyAccountingVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "JourneyAccounting_VersionStructure"

    accounted_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "AccountedObjectRef",
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
    supply_contract_ref: Optional[SupplyContractRef] = field(
        default=None,
        metadata={
            "name": "SupplyContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accounting_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountingCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accounting_type: Optional[JourneyAccountingEnumeration] = field(
        default=None,
        metadata={
            "name": "AccountingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    partial: list[bool] = field(
        default_factory=list,
        metadata={
            "name": "Partial",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
