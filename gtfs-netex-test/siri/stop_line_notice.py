from dataclasses import dataclass

from .stop_line_notice_structure import StopLineNoticeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopLineNotice(StopLineNoticeStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
