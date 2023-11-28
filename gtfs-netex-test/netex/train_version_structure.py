from dataclasses import dataclass, field
from typing import Optional
from netex.train_components_rel_structure import TrainComponentsRelStructure
from netex.train_size import TrainSize
from netex.vehicle_type_version_structure import VehicleTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainVersionStructure(VehicleTypeVersionStructure):
    """
    Type for TRAIN.

    :ivar train_size:
    :ivar components: Ordered collection of TRAIN COMPONENTs making up
        TRAIN.
    """
    class Meta:
        name = "Train_VersionStructure"

    train_size: Optional[TrainSize] = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    components: Optional[TrainComponentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
