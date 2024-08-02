from dataclasses import dataclass

from .notify_by_email_action_structure import NotifyByEmailActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyByEmailAction(NotifyByEmailActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
