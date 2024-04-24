from dataclasses import dataclass, field
from typing import List, Union

from .compound_train import CompoundTrain
from .containment_aggregation_structure import ContainmentAggregationStructure
from .powered_train import PoweredTrain
from .simple_vehicle_type import SimpleVehicleType
from .train import Train
from .transport_type import TransportType
from .unpowered_train import UnpoweredTrain
from .vehicle_type import VehicleType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleTypesInFrame_RelStructure"

    transport_type_dummy_type_or_train_type: List[Union[CompoundTrain, UnpoweredTrain, PoweredTrain, Train, SimpleVehicleType, VehicleType, TransportType]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrain",
                    "type": CompoundTrain,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UnpoweredTrain",
                    "type": UnpoweredTrain,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoweredTrain",
                    "type": PoweredTrain,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleVehicleType",
                    "type": SimpleVehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleType",
                    "type": VehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportType",
                    "type": TransportType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
