from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .payload_publication import PayloadPublication
from .situation import Situation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class SituationPublication(PayloadPublication):
    situation: List[Situation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
