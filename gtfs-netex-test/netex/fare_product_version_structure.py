from dataclasses import dataclass, field
from typing import Optional
from netex.access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.authority_ref import AuthorityRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.charging_moment_enumeration import ChargingMomentEnumeration
from netex.charging_moment_ref import ChargingMomentRef
from netex.condition_summary import ConditionSummary
from netex.fare_product_prices_rel_structure import FareProductPricesRelStructure
from netex.fare_product_ref import FareProductRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from netex.management_agent_ref import ManagementAgentRef
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.service_access_right_version_structure import ServiceAccessRightVersionStructure
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.supplement_product_ref import SupplementProductRef
from netex.tariff_refs_rel_structure import TariffRefsRelStructure
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.travel_agent_ref import TravelAgentRef
from netex.type_of_fare_product_ref import TypeOfFareProductRef
from netex.type_of_fare_product_refs_rel_structure import TypeOfFareProductRefsRelStructure
from netex.usage_discount_right_ref import UsageDiscountRightRef
from netex.validable_elements_rel_structure import ValidableElementsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductVersionStructure(ServiceAccessRightVersionStructure):
    """
    Type for FARE PRODUCT.

    :ivar charging_moment_ref:
    :ivar charging_moment_type: Enumeration of standardised Charging
        moment values _v1.1
    :ivar type_of_fare_product_ref_or_types_of_fare_product:
    :ivar choice:
    :ivar condition_summary:
    :ivar choice_1:
    :ivar
        validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context:
    :ivar validable_elements: VALIDABLE ELEMENTs making up FARE SERVICE
        ACCESS RIGHT.
    :ivar access_rights_in_product: Access rights given by product.
    :ivar tariffs: TARIFFs  used by FARE PRODUCT. These may be derived
        from lower level references.
    :ivar prices: PRICEs  making up FARE PRODUCT.
    """
    class Meta:
        name = "FareProduct_VersionStructure"

    charging_moment_ref: Optional[ChargingMomentRef] = field(
        default=None,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_moment_type: Optional[ChargingMomentEnumeration] = field(
        default=None,
        metadata={
            "name": "ChargingMomentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product_ref_or_types_of_fare_product: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "typesOfFareProduct",
                    "type": TypeOfFareProductRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    condition_summary: Optional[ConditionSummary] = field(
        default=None,
        metadata={
            "name": "ConditionSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice_1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityParameterAssignments",
                    "type": GenericParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    validable_elements: Optional[ValidableElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "validableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_rights_in_product: Optional[AccessRightsInProductRelStructure] = field(
        default=None,
        metadata={
            "name": "accessRightsInProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariffs: Optional[TariffRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[FareProductPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
