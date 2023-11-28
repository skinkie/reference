from dataclasses import dataclass, field
from typing import List
from netex.additional_driver_option import AdditionalDriverOption
from netex.cancelling import Cancelling
from netex.charging_policy import ChargingPolicy
from netex.commercial_profile import CommercialProfile
from netex.companion_profile import CompanionProfile
from netex.eligibility_change_policy import EligibilityChangePolicy
from netex.entitlement_given import EntitlementGiven
from netex.entitlement_required import EntitlementRequired
from netex.exchanging import Exchanging
from netex.frame_containment_structure import FrameContainmentStructure
from netex.frequency_of_use import FrequencyOfUse
from netex.group_ticket import GroupTicket
from netex.interchanging import Interchanging
from netex.luggage_allowance import LuggageAllowance
from netex.minimum_stay import MinimumStay
from netex.penalty_policy import PenaltyPolicy
from netex.purchase_window import PurchaseWindow
from netex.refunding import Refunding
from netex.rental_option import RentalOption
from netex.rental_penalty_policy import RentalPenaltyPolicy
from netex.replacing import Replacing
from netex.reselling import Reselling
from netex.reserving import Reserving
from netex.round_trip import RoundTrip
from netex.routing import Routing
from netex.sales_offer_package_entitlement_given import SalesOfferPackageEntitlementGiven
from netex.sales_offer_package_entitlement_required import SalesOfferPackageEntitlementRequired
from netex.step_limit import StepLimit
from netex.subscribing import Subscribing
from netex.suspending import Suspending
from netex.transferability import Transferability
from netex.usage_validity_period import UsageValidityPeriod
from netex.user_profile import UserProfile
from netex.vehicle_pooler_profile import VehiclePoolerProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageParametersInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of USAGE PARAMETER.
    """
    class Meta:
        name = "usageParametersInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
