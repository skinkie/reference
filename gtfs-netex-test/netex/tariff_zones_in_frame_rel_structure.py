from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_zone import FareZone
from .tariff_zone import TariffZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TariffZonesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "tariffZonesInFrame_RelStructure"

    tariff_zone: list[Union[FareZone, TariffZone]] = field(
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
        },
    )
