from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.driver_trip import DriverTrip

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverTripsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DRIVER TRIPs.
    """
    class Meta:
        name = "driverTripsInFrame_RelStructure"

    driver_trip: List[DriverTrip] = field(
        default_factory=list,
        metadata={
            "name": "DriverTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
