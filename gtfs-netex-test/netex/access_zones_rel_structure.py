from dataclasses import dataclass, field
from typing import Union

from .access_zone import AccessZone
from .access_zone_ref import AccessZoneRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessZonesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessZones_RelStructure"

    access_zone_ref_or_access_zone: list[Union[AccessZoneRef, AccessZone]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZone",
                    "type": AccessZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
