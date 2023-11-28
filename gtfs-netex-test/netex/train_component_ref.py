from dataclasses import dataclass
from netex.train_component_ref_structure import TrainComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainComponentRef(TrainComponentRefStructure):
    """
    Reference to a TRAIN COMPONENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
