from dataclasses import dataclass

from .unpowered_train_version_structure import UnpoweredTrainVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UnpoweredTrain(UnpoweredTrainVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
