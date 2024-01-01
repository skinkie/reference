from dataclasses import dataclass
from .general_frame_member_structure import GeneralFrameMemberStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralFrameMember(GeneralFrameMemberStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
