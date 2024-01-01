from dataclasses import dataclass
from .train_in_compound_train_ref_structure import (
    TrainInCompoundTrainRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainInCompoundTrainRef(TrainInCompoundTrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
