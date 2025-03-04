from dataclasses import dataclass

from .general_frame_member_structure import GeneralFrameMemberStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeneralFrameMember(GeneralFrameMemberStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
