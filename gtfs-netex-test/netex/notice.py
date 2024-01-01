from dataclasses import dataclass
from .notice_version_structure import NoticeVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Notice(NoticeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
