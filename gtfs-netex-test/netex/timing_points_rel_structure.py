from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.garage_point import GaragePoint
from netex.parking_point import ParkingPoint
from netex.relief_point import ReliefPoint
from netex.timing_point import TimingPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPointsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TIMING POINTs.
    """
    class Meta:
        name = "timingPoints_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPoint",
                    "type": TimingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
