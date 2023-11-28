from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.suspension_policy_enumeration import SuspensionPolicyEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SuspendingVersionStructure(UsageParameterVersionStructure):
    """
    Type for SUSPENDING.

    :ivar suspension_policy: Allowed policies for suspending term of
        product.
    :ivar qualification_period: Minimum duration that must have occurred
        before a suspension is allowed.
    :ivar qualification_percent: Minimum proportion of term that must
        have occurred before a suspension is allowed.
    :ivar minimum_suspension_period: Minimum duration allowed for a
        suspension.
    :ivar maximum_suspension_period: Maximum duration allowed for a
        suspension.
    :ivar maximum_number_of_suspensions_per_term: Maximum duration
        allowed for a suspension. with the term of the fare product or
        subscription.
    """
    class Meta:
        name = "Suspending_VersionStructure"

    suspension_policy: List[SuspensionPolicyEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SuspensionPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    qualification_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "QualificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    qualification_percent: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "QualificationPercent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_suspension_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumSuspensionPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_suspension_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumSuspensionPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_suspensions_per_term: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfSuspensionsPerTerm",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
