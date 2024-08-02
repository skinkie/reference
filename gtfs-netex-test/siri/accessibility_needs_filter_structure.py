from dataclasses import dataclass, field
from typing import List

from .user_need_structure import UserNeedStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AccessibilityNeedsFilterStructure:
    user_need: List[UserNeedStructure] = field(
        default_factory=list,
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
