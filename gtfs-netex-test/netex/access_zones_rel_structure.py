from dataclasses import dataclass, field
from typing import List
from netex.access_zone import AccessZone
from netex.access_zone_ref import AccessZoneRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessZonesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ACCESS ZONEs.
    """
    class Meta:
        name = "accessZones_RelStructure"

    access_zone_ref_or_access_zone: List[object] = field(
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
        }
    )
