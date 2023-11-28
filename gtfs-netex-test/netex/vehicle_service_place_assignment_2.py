from dataclasses import dataclass, field
from netex.assignment_version_structure_1 import AssignmentVersionStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePlaceAssignment2(AssignmentVersionStructure1):
    """
    Dummy Type to work round SG restrictions.

    :ivar id: Identifier of VEHICLE SERVICE PLACE ASSIGNMENT.
    """
    class Meta:
        name = "VehicleServicePlaceAssignment_"
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
