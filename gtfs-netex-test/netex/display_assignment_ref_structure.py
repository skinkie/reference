from dataclasses import dataclass, field
from .assignment_ref_structure import AssignmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DisplayAssignmentRefStructure(AssignmentRefStructure):
    order: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    value: RestrictedVar
