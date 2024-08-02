from dataclasses import dataclass

from .publish_to_mobile_action_structure import PublishToMobileActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToMobileAction(PublishToMobileActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
