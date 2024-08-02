from dataclasses import dataclass, field
from typing import List

from .validity_condition_structure import ValidityConditionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class ValidityConditionsStructure:
    validity_condition: List[ValidityConditionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )
