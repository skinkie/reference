from dataclasses import dataclass

from .train_element_type_ref_structure import TrainElementTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TractiveElementTypeRefStructure(TrainElementTypeRefStructure):
    pass
