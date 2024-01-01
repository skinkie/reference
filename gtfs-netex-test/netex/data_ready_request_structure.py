from dataclasses import dataclass
from .abstract_notification_structure import AbstractNotificationStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataReadyRequestStructure(AbstractNotificationStructure):
    pass
