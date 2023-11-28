from dataclasses import dataclass, field
from typing import Optional
from netex.rental_penalty_policy_type_enumeration import RentalPenaltyPolicyTypeEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalPenaltyPolicyVersionStructure(UsageParameterVersionStructure):
    """
    Type for RENTAL PENALTY POLICY.

    :ivar rental_penalty_policy_type: Type of RENTAL PENALTY POLICY
        type.
    :ivar penalty_fee: Transgression results in penalty fee.
    :ivar immobilisation: Transgression results in Immobilisation.
    :ivar disbarring: Transgression results in loss of membership.
    :ivar suspension: Transgression results in suspension of membership.
    """
    class Meta:
        name = "RentalPenaltyPolicy_VersionStructure"

    rental_penalty_policy_type: Optional[RentalPenaltyPolicyTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RentalPenaltyPolicyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    penalty_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PenaltyFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    immobilisation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Immobilisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    disbarring: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Disbarring",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suspension: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Suspension",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
