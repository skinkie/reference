from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegPoint:
    tpeg_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
