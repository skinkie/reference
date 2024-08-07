from dataclasses import dataclass

from .train_component_ref_structure import TrainComponentRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainComponentRef(TrainComponentRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
