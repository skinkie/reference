from dataclasses import dataclass, field
from typing import Optional

from .animal_presence_type_enum import AnimalPresenceTypeEnum
from .extension_type import ExtensionType
from .obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AnimalPresenceObstruction(Obstruction):
    alive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    animal_presence_type: AnimalPresenceTypeEnum = field(
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    animal_presence_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "animalPresenceObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
