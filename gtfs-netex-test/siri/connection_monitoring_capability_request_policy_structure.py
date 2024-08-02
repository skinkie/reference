from dataclasses import dataclass, field
from typing import Optional

from .capability_request_policy_structure import CapabilityRequestPolicyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    foreign_journeys_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForeignJourneysOnly",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
