from dataclasses import dataclass

from .publish_to_display_action_structure import PublishToDisplayActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToDisplayAction(PublishToDisplayActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
