from dataclasses import dataclass

from .train_component_structure import TrainComponentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainComponent(TrainComponentStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
