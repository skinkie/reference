from dataclasses import dataclass
from .general_frame_member_ref_structure import GeneralFrameMemberRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralFrameMemberRef(GeneralFrameMemberRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
