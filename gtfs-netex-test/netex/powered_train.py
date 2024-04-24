from dataclasses import dataclass

from .powered_train_version_structure import PoweredTrainVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PoweredTrain(PoweredTrainVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
