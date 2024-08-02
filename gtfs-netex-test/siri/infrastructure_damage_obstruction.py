from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .infrastructure_damage_type_enum import InfrastructureDamageTypeEnum
from .obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class InfrastructureDamageObstruction(Obstruction):
    infrastructure_damage_type: InfrastructureDamageTypeEnum = field(
        metadata={
            "name": "infrastructureDamageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    infrastructure_damage_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "infrastructureDamageObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
