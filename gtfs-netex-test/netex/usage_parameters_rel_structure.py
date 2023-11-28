from dataclasses import dataclass, field
from typing import List
from netex.additional_driver_option import AdditionalDriverOption
from netex.additional_driver_option_ref import AdditionalDriverOptionRef
from netex.booking_policy_ref import BookingPolicyRef
from netex.cancelling import Cancelling
from netex.cancelling_ref import CancellingRef
from netex.charging_policy import ChargingPolicy
from netex.charging_policy_ref import ChargingPolicyRef
from netex.commercial_profile import CommercialProfile
from netex.commercial_profile_ref import CommercialProfileRef
from netex.companion_profile import CompanionProfile
from netex.companion_profile_ref import CompanionProfileRef
from netex.eligibility_change_policy import EligibilityChangePolicy
from netex.eligibility_change_policy_ref import EligibilityChangePolicyRef
from netex.entitlement_given import EntitlementGiven
from netex.entitlement_given_ref import EntitlementGivenRef
from netex.entitlement_required import EntitlementRequired
from netex.entitlement_required_ref import EntitlementRequiredRef
from netex.exchanging import Exchanging
from netex.exchanging_ref import ExchangingRef
from netex.frequency_of_use import FrequencyOfUse
from netex.frequency_of_use_ref import FrequencyOfUseRef
from netex.group_ticket import GroupTicket
from netex.group_ticket_ref import GroupTicketRef
from netex.interchanging import Interchanging
from netex.interchanging_ref import InterchangingRef
from netex.luggage_allowance import LuggageAllowance
from netex.luggage_allowance_ref import LuggageAllowanceRef
from netex.minimum_stay import MinimumStay
from netex.minimum_stay_ref import MinimumStayRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.penalty_policy import PenaltyPolicy
from netex.penalty_policy_ref import PenaltyPolicyRef
from netex.profile_parameter_ref import ProfileParameterRef
from netex.purchase_window import PurchaseWindow
from netex.purchase_window_ref import PurchaseWindowRef
from netex.refunding import Refunding
from netex.refunding_ref import RefundingRef
from netex.rental_option import RentalOption
from netex.rental_option_ref import RentalOptionRef
from netex.rental_penalty_policy import RentalPenaltyPolicy
from netex.rental_penalty_policy_ref import RentalPenaltyPolicyRef
from netex.replacing import Replacing
from netex.replacing_ref import ReplacingRef
from netex.reselling import Reselling
from netex.reselling_ref import ResellingRef
from netex.reserving import Reserving
from netex.reserving_ref import ReservingRef
from netex.round_trip import RoundTrip
from netex.round_trip_ref import RoundTripRef
from netex.routing import Routing
from netex.routing_ref import RoutingRef
from netex.sales_offer_package_entitlement_given import SalesOfferPackageEntitlementGiven
from netex.sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from netex.sales_offer_package_entitlement_required import SalesOfferPackageEntitlementRequired
from netex.sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from netex.step_limit import StepLimit
from netex.step_limit_ref import StepLimitRef
from netex.subscribing import Subscribing
from netex.subscribing_ref import SubscribingRef
from netex.suspending import Suspending
from netex.suspending_ref import SuspendingRef
from netex.transferability import Transferability
from netex.transferability_ref import TransferabilityRef
from netex.usage_validity_period import UsageValidityPeriod
from netex.usage_validity_period_ref import UsageValidityPeriodRef
from netex.user_profile import UserProfile
from netex.user_profile_ref import UserProfileRef
from netex.vehicle_pooler_profile import VehiclePoolerProfile
from netex.vehicle_pooler_profile_ref import VehiclePoolerProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageParametersRelStructure(OneToManyRelationshipStructure):
    """
    Type for of USAGE PARAMETER.
    """
    class Meta:
        name = "usageParameters_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AdditionalDriverOptionRef",
                    "type": AdditionalDriverOptionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalOptionRef",
                    "type": RentalOptionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalPenaltyPolicyRef",
                    "type": RentalPenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGivenRef",
                    "type": SalesOfferPackageEntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequiredRef",
                    "type": SalesOfferPackageEntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStayRef",
                    "type": MinimumStayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangingRef",
                    "type": InterchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUseRef",
                    "type": FrequencyOfUseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SuspendingRef",
                    "type": SuspendingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriodRef",
                    "type": UsageValidityPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimitRef",
                    "type": StepLimitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingRef",
                    "type": RoutingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTripRef",
                    "type": RoundTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowanceRef",
                    "type": LuggageAllowanceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGivenRef",
                    "type": EntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequiredRef",
                    "type": EntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicyRef",
                    "type": EligibilityChangePolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicketRef",
                    "type": GroupTicketRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileRef",
                    "type": CommercialProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolerProfileRef",
                    "type": VehiclePoolerProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ProfileParameterRef",
                    "type": ProfileParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SubscribingRef",
                    "type": SubscribingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicyRef",
                    "type": PenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicyRef",
                    "type": ChargingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferabilityRef",
                    "type": TransferabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReplacingRef",
                    "type": ReplacingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefundingRef",
                    "type": RefundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangingRef",
                    "type": ExchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResellingRef",
                    "type": ResellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CancellingRef",
                    "type": CancellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReservingRef",
                    "type": ReservingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingPolicyRef",
                    "type": BookingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindowRef",
                    "type": PurchaseWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdditionalDriverOption",
                    "type": AdditionalDriverOption,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalOption",
                    "type": RentalOption,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalPenaltyPolicy",
                    "type": RentalPenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolerProfile",
                    "type": VehiclePoolerProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequired",
                    "type": SalesOfferPackageEntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGiven",
                    "type": SalesOfferPackageEntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStay",
                    "type": MinimumStay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Interchanging",
                    "type": Interchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Suspending",
                    "type": Suspending,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriod",
                    "type": UsageValidityPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUse",
                    "type": FrequencyOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimit",
                    "type": StepLimit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Routing",
                    "type": Routing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTrip",
                    "type": RoundTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowance",
                    "type": LuggageAllowance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequired",
                    "type": EntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGiven",
                    "type": EntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicy",
                    "type": EligibilityChangePolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicket",
                    "type": GroupTicket,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfile",
                    "type": CommercialProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfile",
                    "type": UserProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Subscribing",
                    "type": Subscribing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicy",
                    "type": PenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicy",
                    "type": ChargingPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Cancelling",
                    "type": Cancelling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reserving",
                    "type": Reserving,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindow",
                    "type": PurchaseWindow,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Transferability",
                    "type": Transferability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Replacing",
                    "type": Replacing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Refunding",
                    "type": Refunding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Exchanging",
                    "type": Exchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reselling",
                    "type": Reselling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
