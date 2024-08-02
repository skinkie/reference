from dataclasses import dataclass, field
from typing import List, Optional

from .accessibility_limitation_structure import AccessibilityLimitationStructure
from .extensions_2 import Extensions2
from .suitability_structure import SuitabilityStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class AccessibilityAssessmentStructure:
    mobility_impaired_access: bool = field(
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
    limitations: Optional["AccessibilityAssessmentStructure.Limitations"] = field(
        default=None,
        metadata={
            "name": "Limitations",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    suitabilities: Optional["AccessibilityAssessmentStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass(kw_only=True)
    class Limitations:
        accessibility_limitation: List[AccessibilityLimitationStructure] = field(
            default_factory=list,
            metadata={
                "name": "AccessibilityLimitation",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Suitabilities:
        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "min_occurs": 1,
            },
        )
