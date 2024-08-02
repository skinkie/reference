from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .capability_request_policy_structure import CapabilityRequestPolicyStructure
from .general_message_capability_access_control_structure import GeneralMessageCapabilityAccessControlStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["GeneralMessageServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional[CapabilityRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_control: Optional[GeneralMessageCapabilityAccessControlStructure] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class TopicFiltering:
        default_preview_interval: XmlDuration = field(
            default=XmlDuration("PT60M"),
            metadata={
                "name": "DefaultPreviewInterval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_info_channel: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByInfoChannel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
