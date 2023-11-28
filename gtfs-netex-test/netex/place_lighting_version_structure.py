from dataclasses import dataclass, field
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure
from netex.lighting_enumeration import LightingEnumeration
from netex.lighting_on_method_enumeration import LightingOnMethodEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PlaceLightingVersionStructure(AccessEquipmentVersionStructure):
    """
    Type for a PLACE LIGHTING EQUIPMENT.

    :ivar lighting: Nature of Lighting.
    :ivar always_lit: Whether Place is always lit.
    :ivar lighting_on_method: Method by which lighting is switched on.
        v1.1
    """
    class Meta:
        name = "PlaceLighting_VersionStructure"

    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    always_lit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlwaysLit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lighting_on_method: Optional[LightingOnMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "LightingOnMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
