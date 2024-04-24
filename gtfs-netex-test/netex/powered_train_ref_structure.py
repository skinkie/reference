from dataclasses import dataclass

from .train_ref_structure import TrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PoweredTrainRefStructure(TrainRefStructure):
    pass
