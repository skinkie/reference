from dataclasses import dataclass

from .publish_to_alerts_action_structure import PublishToAlertsActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToAlertsAction(PublishToAlertsActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
