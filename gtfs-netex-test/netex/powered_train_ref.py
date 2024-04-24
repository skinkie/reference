from dataclasses import dataclass

from .powered_train_ref_structure import PoweredTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PoweredTrainRef(PoweredTrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
