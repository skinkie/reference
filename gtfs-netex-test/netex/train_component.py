from dataclasses import dataclass
from .train_component_version_structure import TrainComponentVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponent(TrainComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
