from dataclasses import dataclass, field

from .abstract_topic_permission_structure import AbstractTopicPermissionStructure
from .info_channel_ref_structure import InfoChannelRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoChannelPermissionStructure(AbstractTopicPermissionStructure):
    info_channel_ref: InfoChannelRefStructure = field(
        metadata={
            "name": "InfoChannelRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
