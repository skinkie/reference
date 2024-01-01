from dataclasses import dataclass
from .version_frame_ref_structure import VersionFrameRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompositeFrameRefStructure(VersionFrameRefStructure):
    value: RestrictedVar
