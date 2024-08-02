from dataclasses import dataclass, field
from typing import Optional

from .audible_signals_available import AudibleSignalsAvailable
from .escalator_free_access import EscalatorFreeAccess
from .extensions_2 import Extensions2
from .lift_free_access import LiftFreeAccess
from .step_free_access import StepFreeAccess
from .validity_condition_structure import ValidityConditionStructure
from .visual_signs_available import VisualSignsAvailable
from .wheelchair_access import WheelchairAccess

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class AccessibilityLimitationStructure:
    limitation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LimitationId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    validity_condition: Optional[ValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    wheelchair_access: WheelchairAccess = field(
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
    step_free_access: Optional[StepFreeAccess] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    escalator_free_access: Optional[EscalatorFreeAccess] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    lift_free_access: Optional[LiftFreeAccess] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    audible_signals_available: Optional[AudibleSignalsAvailable] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    visual_signs_available: Optional[VisualSignsAvailable] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
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
