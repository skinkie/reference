from dataclasses import dataclass

from .train_element_version_structure import TrainElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainElement(TrainElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
