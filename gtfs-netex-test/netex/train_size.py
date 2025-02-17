from dataclasses import dataclass

from .train_size_structure import TrainSizeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainSize(TrainSizeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
