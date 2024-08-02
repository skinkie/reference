from dataclasses import dataclass, field

from .abstract_topic_permission_structure import AbstractTopicPermissionStructure
from .connection_link_ref_structure import ConnectionLinkRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionLinkPermissionStructure(AbstractTopicPermissionStructure):
    connection_link_ref: ConnectionLinkRefStructure = field(
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
