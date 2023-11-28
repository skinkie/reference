from dataclasses import dataclass, field
from netex.check_constraint_delay_version_structure import CheckConstraintDelayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintDelay(CheckConstraintDelayVersionStructure):
    """
    Time penalty associated with a CHECK CONSTRAINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
