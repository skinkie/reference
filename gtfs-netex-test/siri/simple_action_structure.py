from dataclasses import dataclass, field
from typing import Optional

from .action_status_enumeration import ActionStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SimpleActionStructure:
    action_status: Optional[ActionStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
