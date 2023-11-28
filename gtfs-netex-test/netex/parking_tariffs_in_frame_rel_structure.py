from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.parking_tariff import ParkingTariff

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingTariffsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of PARKING TARIFFs.

    :ivar parking_tariff: A designated path between two PLACEs. May
        include an Ordered sequence of references to PATH LINKS.
    """
    class Meta:
        name = "parkingTariffsInFrame_RelStructure"

    parking_tariff: List[ParkingTariff] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
