from dataclasses import dataclass, field

from .suitability_enumeration import SuitabilityEnumeration
from .user_need_structure import UserNeedStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class SuitabilityStructure:
    suitable: SuitabilityEnumeration = field(
        metadata={
            "name": "Suitable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
    user_need: UserNeedStructure = field(
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
