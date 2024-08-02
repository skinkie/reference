from dataclasses import dataclass

from .notify_user_action_structure import NotifyUserActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyUserAction(NotifyUserActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
