from dataclasses import dataclass
from .train_version_structure import TrainVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Train(TrainVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
