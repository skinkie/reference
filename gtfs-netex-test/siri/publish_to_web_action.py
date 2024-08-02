from dataclasses import dataclass

from .publish_to_web_action_structure import PublishToWebActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToWebAction(PublishToWebActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
