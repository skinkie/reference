from dataclasses import dataclass, field
from typing import Optional
from netex.individual_traveller_ref import IndividualTravellerRef
from netex.trip_leg_ref import TripLegRef
from netex.trip_ref import TripRef
from netex.validity_parameter_assignment_version_structure import ValidityParameterAssignmentVersionStructure
from netex.vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchaseParameterAssignmentVersionStructure(ValidityParameterAssignmentVersionStructure):
    """
    Type for CustomerPurchase PARAMETER ASSIGNMENT.
    """
    class Meta:
        name = "CustomerPurchaseParameterAssignment_VersionStructure"

    individual_traveller_ref: Optional[IndividualTravellerRef] = field(
        default=None,
        metadata={
            "name": "IndividualTravellerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_pooling_driver_info_ref: Optional[VehiclePoolingDriverInfoRef] = field(
        default=None,
        metadata={
            "name": "VehiclePoolingDriverInfoRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trip_ref: Optional[TripRef] = field(
        default=None,
        metadata={
            "name": "TripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trip_leg_ref: Optional[TripLegRef] = field(
        default=None,
        metadata={
            "name": "TripLegRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
