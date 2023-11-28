from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.rounding_step_ref import RoundingStepRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoundingStepVersionedChildStructure(VersionedChildStructure):
    """
    Type for ROUNDING STEP.

    :ivar rounding_step_ref:
    :ivar round_if_greater_than: Rounding Step Threshold.
    :ivar round_to: Amount to which to round.
    """
    class Meta:
        name = "RoundingStep_VersionedChildStructure"

    rounding_step_ref: Optional[RoundingStepRef] = field(
        default=None,
        metadata={
            "name": "RoundingStepRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    round_if_greater_than: Decimal = field(
        metadata={
            "name": "RoundIfGreaterThan",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    round_to: Decimal = field(
        metadata={
            "name": "RoundTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
