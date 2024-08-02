from dataclasses import dataclass, field

from .abstract_topic_permission_structure import AbstractTopicPermissionStructure
from .operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class OperatorPermissionStructure(AbstractTopicPermissionStructure):
    operator_ref: OperatorRefStructure = field(
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
