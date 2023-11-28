from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.garage_point import GaragePoint
from netex.parking_point import ParkingPoint
from netex.relief_point import ReliefPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReliefPointsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of RELIEF POINTs.
    """
    class Meta:
        name = "reliefPointsInFrame_RelStructure"

    parking_point_or_garage_point_or_relief_point: List[object] = field(
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
            ),
        }
    )
