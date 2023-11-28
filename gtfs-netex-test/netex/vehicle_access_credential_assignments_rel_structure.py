from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_access_credentials_assignment import VehicleAccessCredentialsAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleAccessCredentialAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a VEHICLE ACCESS CREDENTIALs ASSIGNMENT.
    """
    class Meta:
        name = "vehicleAccessCredentialAssignments_RelStructure"

    vehicle_access_credentials_assignment: List[VehicleAccessCredentialsAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleAccessCredentialsAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
