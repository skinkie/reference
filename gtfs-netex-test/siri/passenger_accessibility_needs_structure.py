from dataclasses import dataclass, field
from typing import List, Optional

from .user_need_structure import UserNeedStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class PassengerAccessibilityNeedsStructure:
    user_need: List[UserNeedStructure] = field(
        default_factory=list,
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    accompanied_by_carer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccompaniedByCarer",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
