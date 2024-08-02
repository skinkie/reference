from dataclasses import dataclass, field
from typing import Optional

from .basic_data_value import BasicDataValue
from .extension_type import ExtensionType
from .source import Source
from .validity import Validity

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class ElaboratedData:
    forecast: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    basic_data_value: BasicDataValue = field(
        metadata={
            "name": "basicDataValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    elaborated_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
