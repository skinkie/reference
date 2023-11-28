from dataclasses import dataclass, field
from netex.train_element_version_structure import TrainElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainElement(TrainElementVersionStructure):
    """
    An elementary component of a TRAIN (e.g. wagon, locomotive).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
