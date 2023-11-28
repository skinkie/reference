from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_manoeuvring_requirement import VehicleManoeuvringRequirement
from netex.vehicle_manoeuvring_requirement_ref import VehicleManoeuvringRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleManoeuvringRequirementsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PASSENGER CARRYING REQUIREMENTs.
    """
    class Meta:
        name = "vehicleManoeuvringRequirements_RelStructure"

    vehicle_manoeuvring_requirement_ref_or_vehicle_manoeuvring_requirement: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleManoeuvringRequirementRef",
                    "type": VehicleManoeuvringRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleManoeuvringRequirement",
                    "type": VehicleManoeuvringRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
