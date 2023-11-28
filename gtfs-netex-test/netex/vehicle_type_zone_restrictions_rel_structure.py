from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_type_zone_restriction import VehicleTypeZoneRestriction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeZoneRestrictionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a VEHICLE TYPE ZONE RESTRICTIONs.
    """
    class Meta:
        name = "vehicleTypeZoneRestrictions_RelStructure"

    vehicle_type_zone_restriction: List[VehicleTypeZoneRestriction] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeZoneRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
