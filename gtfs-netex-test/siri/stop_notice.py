from dataclasses import dataclass

from .stop_notice_structure import StopNoticeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopNotice(StopNoticeStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
