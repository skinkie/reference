from dataclasses import dataclass
from .train_component_ref_structure import TrainComponentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentRef(TrainComponentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
