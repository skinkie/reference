from dataclasses import dataclass, field
from typing import Optional
from netex.fare_structure_type_enumeration import FareStructureTypeEnumeration
from netex.operator_restrictions_enumeration import OperatorRestrictionsEnumeration
from netex.tariff_basis_enumeration import TariffBasisEnumeration
from netex.train_restrictions_enumeration import TrainRestrictionsEnumeration
from netex.vehicle_collection_enumeration import VehicleCollectionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConditionSummaryStructure:
    """
    Type for condition summary.

    :ivar fare_structure_type: TypeOfFareCondition.
    :ivar tariff_basis: Basis used to compute  fares.
    :ivar has_notices: Whether the product has NOTICEs associated with
        it.
    :ivar provides_card: Whether the product provdies a card  with it.
    :ivar goes_on_card: Whether the product requires a card to fulfil
        it.
    :ivar is_personal: Whether the product is personaised or anonymous.
    :ivar requires_photo: Whether the product  requires a photo.
    :ivar must_carry: Whether the product  requires the card to be
        carried by the user.
    :ivar requires_account: Whether the product  requires the user to
        register for an account for billing. +v1.1
    :ivar is_supplement: Whether the product is a supplement to another
        product.
    :ivar requires_entitlement: Whether the product requires ENTITLEMENT
        REQUIRED other products.
    :ivar gives_entitlement: Whether the product grants ENTITLEMENT
        REQUIRED other products.
    :ivar has_operator_restrictions: Restictions on which OPERATOR's
        services can be used.
    :ivar has_travel_time_restrictions: Whether there are restictions on
        which routes can be used.
    :ivar has_route_restrictions: Whether there are restictions on which
        routes can be used.
    :ivar train_restrictions: Restictions on which trains can be used.
    :ivar has_zone_restrictions: Whether there are restictions on which
        zones can be used.
    :ivar can_break_journey: Whether the journey can be interrupted by a
        stay at an intermediate station.
    :ivar return_trips_only: Whether the return trip must also be
        purchased.
    :ivar night_train: Whether the trip uses a night Train.
    :ivar can_change_class: Whether the class of usage can  subsequently
        be changed on a ticket.
    :ivar is_refundable: Whether the ticket can be refunded.
    :ivar is_exchangable: Whether the ticket can be exchanged.
    :ivar has_exchange_fee: Whether there is a charge for exchanges.
    :ivar has_discounted_fares: Whether there are any types of
        discounted fare for the FARE PRODUCT.
    :ivar allow_additional_discounts: Whether the product allows
        discounts to be compounded.
    :ivar allow_companion_discounts: Whether the product allows a
        companion discountt for eligible users.
    :ivar has_minimum_price: Whether a minimum price applies to FARE
        PRODUCT.
    :ivar requires_positive_balance: Whether if combined with  other
        products on the same smart card, requires an overall balance for
        any product to work. Eg a Travel Pass may be disabled if the Pay
        as you go for other areas in in arrears.
    :ivar requires_deposit: Requires a deposit +v1.2.2
    :ivar no_cash_payment: Cash payment not accepted +v1.2.2
    :ivar has_purchase_conditions: Whether the  product has purchase
        conditions.
    :ivar has_dynamic_pricing: Whether there is dynamic i.e. yield
        managed pricing for the product.
    :ivar requires_reservation: Whether the product requires a
        reservation.
    :ivar has_reservation_fee: Whether there is a charge for
        reservations.
    :ivar has_quota: Whether the product has  quotas.
    :ivar penalty_if_without_ticket: Whether there is a penalty for
        travelling without a ticket, i.e. tickets can not be bought on-
        board. +v1.1
    :ivar available_on_subscription: Whether the product is available on
        subscription. +v1.1
    :ivar unlimited_mileage: Whether mileage is unlimited. +v1.2.2
    :ivar like_for_like_refuelling: Refuelling Policy +v1.2.2
    :ivar vehicle_collection: Vehicle collection process +v1.2.2
    """
    fare_structure_type: Optional[FareStructureTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FareStructureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_basis: Optional[TariffBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_notices: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasNotices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    provides_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProvidesCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    goes_on_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GoesOnCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_personal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPersonal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_photo: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresPhoto",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    must_carry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MustCarry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_account: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_supplement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSupplement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_entitlement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresEntitlement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gives_entitlement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GivesEntitlement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_operator_restrictions: Optional[OperatorRestrictionsEnumeration] = field(
        default=None,
        metadata={
            "name": "HasOperatorRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_travel_time_restrictions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasTravelTimeRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_route_restrictions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasRouteRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_restrictions: Optional[TrainRestrictionsEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_zone_restrictions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasZoneRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_break_journey: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBreakJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    return_trips_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnTripsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    night_train: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NightTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_change_class: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanChangeClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRefundable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_exchangable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsExchangable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_exchange_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasExchangeFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_discounted_fares: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasDiscountedFares",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allow_additional_discounts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowAdditionalDiscounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allow_companion_discounts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowCompanionDiscounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_minimum_price: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasMinimumPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_positive_balance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresPositiveBalance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_deposit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresDeposit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    no_cash_payment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoCashPayment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_purchase_conditions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasPurchaseConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_dynamic_pricing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasDynamicPricing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_reservation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresReservation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_reservation_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasReservationFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_quota: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasQuota",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    penalty_if_without_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PenaltyIfWithoutTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    available_on_subscription: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvailableOnSubscription",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    unlimited_mileage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    like_for_like_refuelling: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LikeForLikeRefuelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_collection: Optional[VehicleCollectionEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleCollection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
