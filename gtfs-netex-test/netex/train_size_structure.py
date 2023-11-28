from dataclasses import dataclass, field
from typing import Optional
from netex.train_size_enumeration import TrainSizeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainSizeStructure:
    """
    Type for a TRAIN SIZE REQUIREMENT.

    :ivar number_of_cars: Number of cars needed in TRAIN.
    :ivar train_size_type: Nature of Train Size., Short, long, normal.
        Default is normal.
    """
    number_of_cars: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfCars",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_size_type: Optional[TrainSizeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainSizeType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
