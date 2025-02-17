from dataclasses import dataclass

from .abstract_notification_structure import AbstractNotificationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class DataReadyRequestStructure(AbstractNotificationStructure):
    pass
