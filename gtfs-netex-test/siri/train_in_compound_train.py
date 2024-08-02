from dataclasses import dataclass

from .train_in_compound_train_structure import TrainInCompoundTrainStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainInCompoundTrain(TrainInCompoundTrainStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
