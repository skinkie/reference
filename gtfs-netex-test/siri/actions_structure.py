from dataclasses import dataclass, field
from typing import List, Optional

from .manual_action import ManualAction
from .notify_by_email_action import NotifyByEmailAction
from .notify_by_pager_action import NotifyByPagerAction
from .notify_by_sms_action import NotifyBySmsAction
from .notify_user_action import NotifyUserAction
from .publish_to_alerts_action import PublishToAlertsAction
from .publish_to_display_action import PublishToDisplayAction
from .publish_to_mobile_action import PublishToMobileAction
from .publish_to_tv_action import PublishToTvAction
from .publish_to_web_action import PublishToWebAction
from .publishing_action_structure import PublishingActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ActionsStructure:
    publish_to_web_action: List[PublishToWebAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToWebAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_mobile_action: List[PublishToMobileAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToMobileAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_tv_action: List[PublishToTvAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToTvAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_alerts_action: List[PublishToAlertsAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToAlertsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_display_action: List[PublishToDisplayAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToDisplayAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    manual_action: List[ManualAction] = field(
        default_factory=list,
        metadata={
            "name": "ManualAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_email_action: List[NotifyByEmailAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByEmailAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_sms_action: List[NotifyBySmsAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyBySmsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_pager_action: List[NotifyByPagerAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByPagerAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_user_action: List[NotifyUserAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyUserAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publishing_action: List[PublishingActionStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublishingAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
