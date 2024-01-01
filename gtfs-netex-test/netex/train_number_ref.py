from dataclasses import dataclass
from .train_number_ref_structure import TrainNumberRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainNumberRef(TrainNumberRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
