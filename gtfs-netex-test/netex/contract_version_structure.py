from dataclasses import dataclass, field
from typing import List, Optional, Union

from .authority import Authority
from .entity_in_version_structure import DataManagedObjectStructure
from .general_organisation import GeneralOrganisation
from .info_links_rel_structure import InfoLinksRelStructure
from .legal_status_enumeration import LegalStatusEnumeration
from .management_agent import ManagementAgent
from .multilingual_string import MultilingualString
from .online_service_operator import OnlineServiceOperator
from .operator import Operator
from .other_organisation import OtherOrganisation
from .retail_consortium import RetailConsortium
from .serviced_organisation import ServicedOrganisation
from .travel_agent import TravelAgent
from .type_of_contract_enumeration import TypeOfContractEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContractVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Contract_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    type_of_contract: Optional[TypeOfContractEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    legal_status: Optional[LegalStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "LegalStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contract_governing_law: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ContractGoverningLaw",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contractors: "ContractVersionStructure.Contractors" = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    contractees: "ContractVersionStructure.Contractees" = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    contract_documents: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "contractDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class Contractors:
        organisation_or_transport_organisation: List[
            Union[
                RetailConsortium,
                ServicedOrganisation,
                GeneralOrganisation,
                ManagementAgent,
                TravelAgent,
                OtherOrganisation,
                OnlineServiceOperator,
                Authority,
                Operator,
            ]
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "RetailConsortium",
                        "type": RetailConsortium,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ServicedOrganisation",
                        "type": ServicedOrganisation,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "GeneralOrganisation",
                        "type": GeneralOrganisation,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ManagementAgent",
                        "type": ManagementAgent,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "TravelAgent",
                        "type": TravelAgent,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "OtherOrganisation",
                        "type": OtherOrganisation,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "OnlineServiceOperator",
                        "type": OnlineServiceOperator,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "Authority",
                        "type": Authority,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "Operator",
                        "type": Operator,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class Contractees:
        organisation_or_transport_organisation: List[
            Union[
                RetailConsortium,
                ServicedOrganisation,
                GeneralOrganisation,
                ManagementAgent,
                TravelAgent,
                OtherOrganisation,
                OnlineServiceOperator,
                Authority,
                Operator,
            ]
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "RetailConsortium",
                        "type": RetailConsortium,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ServicedOrganisation",
                        "type": ServicedOrganisation,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "GeneralOrganisation",
                        "type": GeneralOrganisation,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ManagementAgent",
                        "type": ManagementAgent,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "TravelAgent",
                        "type": TravelAgent,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "OtherOrganisation",
                        "type": OtherOrganisation,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "OnlineServiceOperator",
                        "type": OnlineServiceOperator,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "Authority",
                        "type": Authority,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "Operator",
                        "type": Operator,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
