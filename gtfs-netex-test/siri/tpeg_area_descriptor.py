from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_descriptor import TpegDescriptor
from .tpeg_loc03_area_descriptor_subtype_enum import TpegLoc03AreaDescriptorSubtypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegAreaDescriptor(TpegDescriptor):
    tpeg_area_descriptor_type: TpegLoc03AreaDescriptorSubtypeEnum = field(
        metadata={
            "name": "tpegAreaDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_area_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
