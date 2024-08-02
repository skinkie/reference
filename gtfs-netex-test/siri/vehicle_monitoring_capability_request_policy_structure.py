from dataclasses import dataclass, field
from typing import Optional

from .capability_request_policy_structure import CapabilityRequestPolicyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    has_references: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasReferences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    has_names: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasNames",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
