from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_type_zone_restriction_ref import VehicleTypeZoneRestrictionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeZoneRestrictionRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLE TYPE ZONE RESTRICTIONs.
    """
    class Meta:
        name = "vehicleTypeZoneRestrictionRefs_RelStructure"

    vehicle_type_zone_restriction_ref: List[VehicleTypeZoneRestrictionRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeZoneRestrictionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
