from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_loc03_other_point_descriptor_subtype_enum import TpegLoc03OtherPointDescriptorSubtypeEnum
from .tpeg_point_descriptor import TpegPointDescriptor

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegOtherPointDescriptor(TpegPointDescriptor):
    tpeg_other_point_descriptor_type: TpegLoc03OtherPointDescriptorSubtypeEnum = field(
        metadata={
            "name": "tpegOtherPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_other_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
