from dataclasses import dataclass, field
from typing import Optional
from .activation_assignments_rel_structure import (
    ActivationAssignmentsRelStructure,
)
from .equipment_version_structure import EquipmentVersionStructure
from .traffic_control_point_ref import TrafficControlPointRef
from .type_of_activation_ref import TypeOfActivationRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivatedEquipmentVersionStructure(EquipmentVersionStructure):
    class Meta:
        name = "ActivatedEquipment_VersionStructure"

    traffic_control_point_ref: Optional[TrafficControlPointRef] = field(
        default=None,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_activation_ref: Optional[TypeOfActivationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assignments: Optional[ActivationAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
