from dataclasses import dataclass

from .notify_by_sms_action_structure import NotifyBySmsActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyBySmsAction(NotifyBySmsActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
