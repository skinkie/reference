from dataclasses import dataclass, field
from typing import Optional, Union

from .entity_in_version_structure import VersionedChildStructure
from .fare_zone_ref import FareZoneRef
from .tariff_zone_ref import TariffZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZoneInSeriesVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "ZoneInSeries_VersionedChildStructure"

    tariff_zone_ref: Optional[Union[FareZoneRef, TariffZoneRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    interchange_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterchangeAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
