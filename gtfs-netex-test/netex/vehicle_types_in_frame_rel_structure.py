from dataclasses import dataclass, field
from typing import List
from netex.compound_train import CompoundTrain
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.simple_vehicle_type import SimpleVehicleType
from netex.train import Train
from netex.vehicle_type import VehicleType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE TYPEs.
    """
    class Meta:
        name = "vehicleTypesInFrame_RelStructure"

    choice: List[object] = field(
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
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleType",
                    "type": VehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleVehicleType",
                    "type": SimpleVehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
