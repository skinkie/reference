from dataclasses import dataclass, field
from typing import List, Optional
from netex.partial_refund_basis_enumeration import PartialRefundBasisEnumeration
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.refund_policy_enumeration import RefundPolicyEnumeration
from netex.refund_type_enumeration import RefundTypeEnumeration
from netex.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RefundingVersionStructure(ResellingVersionStructure):
    """
    Type for REFUNDING.

    :ivar refund_type: Type of Refund.
    :ivar refund_policy: Reasons for giving refunds. +v1.1
    :ivar partial_refund_basis: Basis on which partial refunds of period
        passes etc. are calculated. +v1.1
    :ivar payment_method: DEPRECATED - use PaymentMethods on RESELLING
    """
    class Meta:
        name = "Refunding_VersionStructure"

    refund_type: Optional[RefundTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refund_policy: List[RefundPolicyEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RefundPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    partial_refund_basis: Optional[PartialRefundBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "PartialRefundBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_method: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
