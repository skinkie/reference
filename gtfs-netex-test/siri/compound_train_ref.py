from dataclasses import dataclass

from .compound_train_ref_structure import CompoundTrainRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CompoundTrainRef(CompoundTrainRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
