from dataclasses import dataclass
from .composite_frame_ref_structure import CompositeFrameRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompositeFrameRef(CompositeFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
