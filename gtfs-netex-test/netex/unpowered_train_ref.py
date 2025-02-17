from dataclasses import dataclass

from .unpowered_train_ref_structure import UnpoweredTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class UnpoweredTrainRef(UnpoweredTrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
