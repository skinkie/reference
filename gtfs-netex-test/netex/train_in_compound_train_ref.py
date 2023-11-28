from dataclasses import dataclass
from netex.train_in_compound_train_ref_structure import TrainInCompoundTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainInCompoundTrainRef(TrainInCompoundTrainRefStructure):
    """
    Reference to a TRAIN IN COMPOUND TRAIN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
