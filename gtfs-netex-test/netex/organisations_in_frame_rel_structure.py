from dataclasses import dataclass, field
from typing import List
from netex.authority import Authority
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.general_organisation import GeneralOrganisation
from netex.management_agent import ManagementAgent
from netex.online_service_operator import OnlineServiceOperator
from netex.operator import Operator
from netex.other_organisation import OtherOrganisation
from netex.retail_consortium import RetailConsortium
from netex.serviced_organisation import ServicedOrganisation
from netex.travel_agent import TravelAgent

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ORGANISATION.
    """
    class Meta:
        name = "organisationsInFrame_RelStructure"

    choice: List[object] = field(
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
        }
    )
