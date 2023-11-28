from dataclasses import dataclass
from netex.train_number_ref_structure import TrainNumberRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainNumberRef(TrainNumberRefStructure):
    """
    Reference to a TRAIN NUMBER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
