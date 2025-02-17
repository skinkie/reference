from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .driver_trip import DriverTrip

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DriverTripsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "driverTripsInFrame_RelStructure"

    driver_trip: list[DriverTrip] = field(
        default_factory=list,
        metadata={
            "name": "DriverTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
