from dataclasses import dataclass
from netex.access_right_parameter_assignment_ref_structure import AccessRightParameterAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeviceParameterAssignmentRefStructure(AccessRightParameterAssignmentRefStructure):
    """
    Type for Reference to a DEVICE PARAMETER.
    """
