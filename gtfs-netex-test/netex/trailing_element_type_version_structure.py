from dataclasses import dataclass

from .train_element_type_version_structure import TrainElementTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrailingElementTypeVersionStructure(TrainElementTypeVersionStructure):
    class Meta:
        name = "TrailingElementType_VersionStructure"
