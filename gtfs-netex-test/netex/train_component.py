from dataclasses import dataclass, field
from netex.train_component_version_structure import TrainComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainComponent(TrainComponentVersionStructure):
    """
    A specification of the order of TRAIN ELEMENTs in a TRAIN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
