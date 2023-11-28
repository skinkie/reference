from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.effective_from_enumeration import EffectiveFromEnumeration
from netex.empty_type_2 import EmptyType2
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.per_basis_enumeration import PerBasisEnumeration
from netex.resell_type_enumeration import ResellTypeEnumeration
from netex.resell_when_enumeration import ResellWhenEnumeration
from netex.time_interval_ref_structure import TimeIntervalRefStructure
from netex.type_of_payment_method_refs_rel_structure import TypeOfPaymentMethodRefsRelStructure
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResellingVersionStructure(UsageParameterVersionStructure):
    """
    Type for RESELLING.

    :ivar allowed: Whether ticket can be resold (ie refunded or
        exchanged respectively)
    :ivar can_change_class: Whether transaction to change class of
        ticket is allowed.
    :ivar unused_tickets_only: Whether only full tickets can be resold.
    :ivar only_at_certain_distribution_points: Whether reselling can
        only be done in certain places.
    :ivar resell_when: Event marking when there is resell status of the
        ticket changes.
    :ivar
        exchangable_from_any_time_or_exchangable_from_duration_or_exchangable_from_percent_use:
    :ivar exchangable_from_interval_ref: Reference to arbitrary
        TimeInterval determining period from which reselling can be done
        relative to trigger point.
    :ivar
        exchangable_until_any_time_or_exchangable_until_duration_or_exchangable_until_percent_use:
    :ivar exchangable_until_interval_ref: Reference to arbitrary
        TimeInterval determining period up until which reselling can be
        done relative to trigger point.
    :ivar effective_from: Constraint on when change can be made +v1.1
    :ivar notification_period: Notice period needed before transaction
        can be made. + v1.1
    :ivar has_fee: Whether these is a fee for a resale.
    :ivar refund_basis: Basis on which resale is made.
    :ivar payment_methods: PAYMENT METHODs allowed to pay fee or to make
        refund.
    :ivar types_of_payment_method_ref: Other PAYMENT METHODs allowd to
        pay fee or to make refund.
    """
    class Meta:
        name = "Reselling_VersionStructure"

    allowed: Optional[ResellTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "Allowed",
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
    unused_tickets_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnusedTicketsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    only_at_certain_distribution_points: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnlyAtCertainDistributionPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    resell_when: Optional[ResellWhenEnumeration] = field(
        default=None,
        metadata={
            "name": "ResellWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_from_any_time_or_exchangable_from_duration_or_exchangable_from_percent_use: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExchangableFromAnyTime",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableFromDuration",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableFromPercentUse",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    exchangable_from_interval_ref: Optional[TimeIntervalRefStructure] = field(
        default=None,
        metadata={
            "name": "ExchangableFromIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_until_any_time_or_exchangable_until_duration_or_exchangable_until_percent_use: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExchangableUntilAnyTime",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableUntilDuration",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableUntilPercentUse",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    exchangable_until_interval_ref: Optional[TimeIntervalRefStructure] = field(
        default=None,
        metadata={
            "name": "ExchangableUntilIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    effective_from: Optional[EffectiveFromEnumeration] = field(
        default=None,
        metadata={
            "name": "EffectiveFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notification_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "NotificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refund_basis: Optional[PerBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "RefundBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    types_of_payment_method_ref: Optional[TypeOfPaymentMethodRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
