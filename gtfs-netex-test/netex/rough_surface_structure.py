from dataclasses import dataclass, field
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure
from netex.surface_type_enumeration import SurfaceTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoughSurfaceStructure(AccessEquipmentVersionStructure):
    """
    Type for a ROUGH SURFACE.

    :ivar surface_type: Type of Surface.
    :ivar suitable_for_cycles: Whether equipment is suitable for cycles.
    """
    surface_type: SurfaceTypeEnumeration = field(
        metadata={
            "name": "SurfaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
