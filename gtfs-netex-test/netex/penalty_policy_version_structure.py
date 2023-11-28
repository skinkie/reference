from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.penalty_policy_type_enumeration import PenaltyPolicyTypeEnumeration
from netex.same_station_reentry_policy_enumeration import SameStationReentryPolicyEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PenaltyPolicyVersionStructure(UsageParameterVersionStructure):
    """
    Type for PENALTY POLICY.

    :ivar penalty_policy_type: Type of PENALTY POLICY type.
    :ivar same_station_rentry_policy: Policy on rentering at same
        station within a limited period.
    :ivar minimum_time_before_reentry: Minimum time before reentry at
        the same station.
    :ivar maximum_number_of_fail_to_check_out_events: Lmit on the
        number of fail-to-checkout events allowed before suspension.
        +v1.1
    """
    class Meta:
        name = "PenaltyPolicy_VersionStructure"

    penalty_policy_type: Optional[PenaltyPolicyTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PenaltyPolicyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    same_station_rentry_policy: Optional[SameStationReentryPolicyEnumeration] = field(
        default=None,
        metadata={
            "name": "SameStationRentryPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_time_before_reentry: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTimeBeforeReentry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_fail_to_check_out_events: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfFailToCheckOutEvents",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
