from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fare_zone import FareZone
from netex.tariff_zone import TariffZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TariffZonesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TARIFF ZONEs.
    """
    class Meta:
        name = "tariffZonesInFrame_RelStructure"

    fare_zone_or_tariff_zone: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareZone",
                    "type": FareZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZone",
                    "type": TariffZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
