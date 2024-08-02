from dataclasses import dataclass, field
from typing import Optional

from .cause import Cause
from .cause_type_enum import CauseTypeEnum
from .extension_type import ExtensionType
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class NonManagedCause(Cause):
    cause_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "causeDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    cause_type: Optional[CauseTypeEnum] = field(
        default=None,
        metadata={
            "name": "causeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    non_managed_cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonManagedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
