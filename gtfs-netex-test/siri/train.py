from dataclasses import dataclass

from .train_structure import TrainStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Train(TrainStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
