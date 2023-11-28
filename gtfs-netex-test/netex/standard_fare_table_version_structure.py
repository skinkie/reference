from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate
from netex.authority_ref import AuthorityRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.management_agent_ref import ManagementAgentRef
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.rounding_ref import RoundingRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.travel_agent_ref import TravelAgentRef
from netex.type_of_fare_table_ref import TypeOfFareTableRef
from netex.used_in_refs_rel_structure import UsedInRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StandardFareTableVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a STANDARD FARE TABLE PRICE GROUP.

    :ivar start_date: Start date for PRICE GROUP.
    :ivar end_date: End date for PRICE GROUP.
    :ivar rounding_ref:
    :ivar type_of_fare_table_ref:
    :ivar prices_for: Combination of Elements for which this table
        provides PRICEs.
    :ivar used_in: Elements that use FARE TABLE that are not PRICEABLE
        OBJECTs.
    :ivar choice:
    :ivar first_class_single: Price for a first class single  fare.
    :ivar second_class_single: Price for a second class  single fare.
    :ivar first_class_return: Price for a first class return fare.
    :ivar second_class_return: Price for a second class return fare.
    """
    class Meta:
        name = "StandardFareTable_VersionStructure"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_table_ref: Optional[TypeOfFareTableRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices_for: Optional[PriceableObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "pricesFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    used_in: Optional[UsedInRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
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
    first_class_single: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    second_class_single: Decimal = field(
        metadata={
            "name": "SecondClassSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    first_class_return: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassReturn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    second_class_return: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SecondClassReturn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
