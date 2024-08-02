from dataclasses import dataclass

from .notify_by_pager_action_structure import NotifyByPagerActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NotifyByPagerAction(NotifyByPagerActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
