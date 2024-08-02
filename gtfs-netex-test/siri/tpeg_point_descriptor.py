from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_descriptor import TpegDescriptor

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegPointDescriptor(TpegDescriptor):
    tpeg_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
