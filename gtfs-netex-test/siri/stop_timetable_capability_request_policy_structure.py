from dataclasses import dataclass, field
from typing import Optional

from .capability_request_policy_structure import CapabilityRequestPolicyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    use_references: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseReferences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    use_names: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseNames",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
