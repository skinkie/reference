from dataclasses import dataclass, field
from typing import Optional

from .abstract_referencing_item_structure import AbstractReferencingItemStructure
from .extensions_1 import Extensions1
from .info_channel_ref_structure import InfoChannelRefStructure
from .info_message_ref_structure import InfoMessageRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoMessageCancellationStructure(AbstractReferencingItemStructure):
    info_message_identifier: InfoMessageRefStructure = field(
        metadata={
            "name": "InfoMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    info_channel_ref: Optional[InfoChannelRefStructure] = field(
        default=None,
        metadata={
            "name": "InfoChannelRef",
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
