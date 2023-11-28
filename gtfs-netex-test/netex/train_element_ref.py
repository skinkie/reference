from dataclasses import dataclass
from netex.train_element_ref_structure import TrainElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainElementRef(TrainElementRefStructure):
    """
    Reference to a TRAIN ELEMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
