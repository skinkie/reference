from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.limitation_status_enumeration import LimitationStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityLimitationVersionedChildStructure(VersionedChildStructure):
    """
    Type for an ACCESSIBILITY LIMITATION.

    :ivar wheelchair_access:
    :ivar step_free_access:
    :ivar escalator_free_access:
    :ivar lift_free_access:
    :ivar audible_signals_available: Whether a PLACE has audible signals
        for the visually impaired.
    :ivar visual_signs_available: Whether a PLACE has visual signals for
        the hearing impaired.
    """
    class Meta:
        name = "AccessibilityLimitation_VersionedChildStructure"

    wheelchair_access: LimitationStatusEnumeration = field(
        default=LimitationStatusEnumeration.FALSE,
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    step_free_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    escalator_free_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lift_free_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audible_signals_available: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visual_signs_available: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
