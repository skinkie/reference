from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .general_instruction_to_road_users_type_enum import GeneralInstructionToRoadUsersTypeEnum
from .network_management import NetworkManagement

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class GeneralInstructionToRoadUsers(NetworkManagement):
    general_instruction_to_road_users_type: GeneralInstructionToRoadUsersTypeEnum = field(
        metadata={
            "name": "generalInstructionToRoadUsersType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    general_instruction_to_road_users_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalInstructionToRoadUsersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
