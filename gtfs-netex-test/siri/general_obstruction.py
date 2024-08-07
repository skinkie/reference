from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .group_of_people_involved import GroupOfPeopleInvolved
from .obstruction import Obstruction
from .obstruction_type_enum import ObstructionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class GeneralObstruction(Obstruction):
    obstruction_type: List[ObstructionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "obstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    general_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
