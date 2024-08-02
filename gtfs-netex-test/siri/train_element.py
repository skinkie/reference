from dataclasses import dataclass

from .train_element_structure import TrainElementStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainElement(TrainElementStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
