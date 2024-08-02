from dataclasses import dataclass, field
from typing import Optional

from .exchange import Exchange
from .extension_type import ExtensionType
from .payload_publication import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class D2LogicalModel1:
    class Meta:
        name = "D2LogicalModel"

    exchange: Exchange = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    payload_publication: Optional[PayloadPublication] = field(
        default=None,
        metadata={
            "name": "payloadPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    d2_logical_model_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "d2LogicalModelExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    model_base_version: str = field(
        init=False,
        default="2.0RC1",
        metadata={
            "name": "modelBaseVersion",
            "type": "Attribute",
            "required": True,
        },
    )
