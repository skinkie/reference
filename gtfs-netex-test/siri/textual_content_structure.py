from dataclasses import dataclass, field
from typing import List, Optional

from .consequence_content_structure import ConsequenceContentStructure
from .defaulted_text_structure import DefaultedTextStructure
from .description_content_structure import DescriptionContentStructure
from .duration_content_structure import DurationContentStructure
from .image_structure import ImageStructure
from .info_link_structure_2 import InfoLinkStructure2
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
from .reason_content_structure import ReasonContentStructure
from .recommendation_content_structure import RecommendationContentStructure
from .remark_content_structure import RemarkContentStructure
from .summary_content_structure import SummaryContentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TextualContentStructure:
    textual_content_size: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TextualContentSize",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
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
    summary_content: SummaryContentStructure = field(
        metadata={
            "name": "SummaryContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    reason_content: Optional[ReasonContentStructure] = field(
        default=None,
        metadata={
            "name": "ReasonContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description_content: List[DescriptionContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consequence_content: List[ConsequenceContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConsequenceContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    recommendation_content: List[RecommendationContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "RecommendationContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    duration_content: Optional[DurationContentStructure] = field(
        default=None,
        metadata={
            "name": "DurationContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    remark_content: List[RemarkContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "RemarkContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_link: List[InfoLinkStructure2] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    image: List[ImageStructure] = field(
        default_factory=list,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    internal: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
