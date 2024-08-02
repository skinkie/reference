from dataclasses import dataclass

from .train_ref_structure import TrainRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainRef(TrainRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
