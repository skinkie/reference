from dataclasses import dataclass
from .train_component_label_assignment_ref_structure import (
    TrainComponentLabelAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentLabelAssignmentRef(
    TrainComponentLabelAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
