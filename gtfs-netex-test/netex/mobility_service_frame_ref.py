from dataclasses import dataclass
from .mobility_service_frame_ref_structure import (
    MobilityServiceFrameRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobilityServiceFrameRef(MobilityServiceFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
