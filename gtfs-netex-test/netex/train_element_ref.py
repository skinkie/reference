from dataclasses import dataclass
from .train_element_ref_structure import TrainElementRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainElementRef(TrainElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
