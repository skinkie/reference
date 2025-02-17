from dataclasses import dataclass

from .type_of_notice_ref_structure import TypeOfNoticeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfNoticeRef(TypeOfNoticeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
