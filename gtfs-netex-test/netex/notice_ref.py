from dataclasses import dataclass
from netex.notice_ref_structure import NoticeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticeRef(NoticeRefStructure):
    """
    Reference to a NOTICE i.e. footnote, note,  announcement or other informational
    text element.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
