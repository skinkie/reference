from dataclasses import dataclass, field
from netex.activation_assignment_version_structure import ActivationAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationAssignment(ActivationAssignmentVersionStructure):
    """An assignment of an ACTIVATION POINT/LINK to an ACTIVATED EQUIPMENT related
    on its turn to a TRAFFIC CONTROL POINT.

    The considered ACTIVATION POINT/LINK will be used to influence the
    control process for that TRAFFIC CONTROL POINT (e.g. to fix
    priorities as regards the processing of competing requests from
    different ACTIVATION POINTs/LINKs).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
