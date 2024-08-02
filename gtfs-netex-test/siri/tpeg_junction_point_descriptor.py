from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .tpeg_loc03_junction_point_descriptor_subtype_enum import TpegLoc03JunctionPointDescriptorSubtypeEnum
from .tpeg_point_descriptor import TpegPointDescriptor

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TpegJunctionPointDescriptor(TpegPointDescriptor):
    tpeg_junction_point_descriptor_type: TpegLoc03JunctionPointDescriptorSubtypeEnum = field(
        metadata={
            "name": "tpegJunctionPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_junction_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
