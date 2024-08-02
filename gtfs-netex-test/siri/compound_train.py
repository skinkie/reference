from dataclasses import dataclass

from .compound_train_structure import CompoundTrainStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CompoundTrain(CompoundTrainStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
