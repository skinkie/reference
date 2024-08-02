from dataclasses import dataclass, field
from typing import Optional

from .area_of_interest_enum import AreaOfInterestEnum
from .confidentiality_value_enum import ConfidentialityValueEnum
from .extension_type import ExtensionType
from .information_status_enum import InformationStatusEnum
from .urgency_enum import UrgencyEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class HeaderInformation:
    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "areaOfInterest",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    confidentiality: ConfidentialityValueEnum = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    information_status: InformationStatusEnum = field(
        metadata={
            "name": "informationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    urgency: Optional[UrgencyEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    header_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "headerInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
