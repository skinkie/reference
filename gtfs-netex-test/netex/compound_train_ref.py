from dataclasses import dataclass
from netex.compound_train_ref_structure import CompoundTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompoundTrainRef(CompoundTrainRefStructure):
    """
    Reference to a COMPOUND TRAIN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
