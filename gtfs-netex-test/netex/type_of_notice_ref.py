from dataclasses import dataclass
from netex.type_of_notice_ref_structure import TypeOfNoticeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfNoticeRef(TypeOfNoticeRefStructure):
    """
    Reference to a TYPE OF NOTICe.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
