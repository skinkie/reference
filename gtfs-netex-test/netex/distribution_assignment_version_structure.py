from dataclasses import dataclass, field
from typing import List, Optional
from netex.all_authorities_ref import AllAuthoritiesRef
from netex.all_countries_ref import AllCountriesRef
from netex.all_distribution_channels_ref import AllDistributionChannelsRef
from netex.all_operators_ref import AllOperatorsRef
from netex.all_organisations_ref import AllOrganisationsRef
from netex.all_public_transport_organisations_ref import AllPublicTransportOrganisationsRef
from netex.all_transport_organisations_ref import AllTransportOrganisationsRef
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.assignment_version_structure_2 import AssignmentVersionStructure2
from netex.authority_ref import AuthorityRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.country_ref import CountryRef
from netex.distribution_channel_ref import DistributionChannelRef
from netex.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.distribution_rights_enumeration import DistributionRightsEnumeration
from netex.entitlement_product_ref import EntitlementProductRef
from netex.fare_product_ref import FareProductRef
from netex.fulfilment_method_ref import FulfilmentMethodRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from netex.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.management_agent_ref import ManagementAgentRef
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.responsibility_set_ref import ResponsibilitySetRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.service_access_right_ref import ServiceAccessRightRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.supplement_product_ref import SupplementProductRef
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.topographic_place_ref import TopographicPlaceRef
from netex.travel_agent_ref import TravelAgentRef
from netex.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistributionAssignmentVersionStructure(AssignmentVersionStructure2):
    """
    Type for DISTRIBUTION ASSIGNMENT.

    :ivar choice:
    :ivar sales_offer_package_ref:
    :ivar group_of_sales_offer_packages_ref:
    :ivar distribution_rights: Override the folloing   rights allowed by
        channel.
    :ivar all_countries_ref_or_country_ref:
    :ivar allowed_in_country: Whether distribution is allowed or
        forbidden for given country.
    :ivar topographic_place_ref:
    :ivar
        all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref:
    :ivar distribution_channel_type: Classification of  DISTRIBUTION
        CHANNEL.
    :ivar allowed_in_channel: Whether distribution is allowed or
        forbidden for given channel.
    :ivar restricted_to_channel: Whether distribution is restricted to a
        given country and / or channel.
    :ivar mandatory_product: Whether product is mandatory, i.e.  must be
        provided.
    :ivar initial_carrier: Wehther initial carrer has rights.
    :ivar transit_carrier: Whther intremediate transit carrier has
        rights.
    :ivar final_carrier: Whetehr final carrier has rights.
    :ivar choice_1:
    :ivar responsibility_set_ref:
    :ivar ticketing_service_facility_list:
    :ivar payment_methods: Payment methods allowed. May override Channel
        to be more specific.
    :ivar requires_registration: Whetee fDistribution requires the user
        to register.
    :ivar fulfilment_method_ref:
    :ivar notice_assignments: NOTICEs for  SALES PACKAGe.
    """
    class Meta:
        name = "DistributionAssignment_VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_sales_offer_packages_ref: Optional[GroupOfSalesOfferPackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_rights: List[DistributionRightsEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DistributionRights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    all_countries_ref_or_country_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllCountriesRef",
                    "type": AllCountriesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CountryRef",
                    "type": CountryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    allowed_in_country: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowedInCountry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllDistributionChannelsRef",
                    "type": AllDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    distribution_channel_type: Optional[DistributionChannelTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DistributionChannelType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_in_channel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowedInChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restricted_to_channel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RestrictedToChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mandatory_product: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MandatoryProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    initial_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InitialCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transit_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TransitCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    final_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinalCarrier",
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
                    "name": "AllAuthoritiesRef",
                    "type": AllAuthoritiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOperatorsRef",
                    "type": AllOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllPublicTransportOrganisationsRef",
                    "type": AllPublicTransportOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllTransportOrganisationsRef",
                    "type": AllTransportOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOrganisationsRef",
                    "type": AllOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
    responsibility_set_ref: Optional[ResponsibilitySetRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_service_facility_list: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    requires_registration: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresRegistration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_ref: Optional[FulfilmentMethodRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
