from dataclasses import dataclass, field
from netex.train_version_structure import TrainVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Train(TrainVersionStructure):
    """
    A vehicle composed of TRAIN ELEMENTs in a certain order, i.e. of wagons
    assembled together and propelled by a locomotive or one of the wagons.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
