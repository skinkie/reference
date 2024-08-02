from dataclasses import dataclass

from .train_in_compound_train_ref_structure import TrainInCompoundTrainRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainInCompoundTrainRef(TrainInCompoundTrainRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
