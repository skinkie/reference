from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .abstract_identified_item_structure import AbstractIdentifiedItemStructure
from .extensions_1 import Extensions1
from .info_channel_ref_structure import InfoChannelRefStructure
from .info_message_ref_structure import InfoMessageRefStructure
from .situation_ref import SituationRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoMessageStructure(AbstractIdentifiedItemStructure):
    info_message_identifier: InfoMessageRefStructure = field(
        metadata={
            "name": "InfoMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    info_message_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "InfoMessageVersion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_channel_ref: Optional[InfoChannelRefStructure] = field(
        default=None,
        metadata={
            "name": "InfoChannelRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    content: Optional[object] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    format_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatRef",
            "type": "Attribute",
        },
    )
