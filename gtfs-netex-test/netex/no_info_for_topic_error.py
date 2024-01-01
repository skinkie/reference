from dataclasses import dataclass
from .no_info_for_topic_error_structure import NoInfoForTopicErrorStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NoInfoForTopicError(NoInfoForTopicErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
