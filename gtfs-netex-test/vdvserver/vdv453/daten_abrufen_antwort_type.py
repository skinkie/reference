from dataclasses import dataclass, field
from typing import List, Optional, Union
from .abbringernachricht_type import AbbringernachrichtType
from .andnachricht_type import AndnachrichtType
from .ausnachricht_type import AusnachrichtType
from .azbnachricht_type import AzbnachrichtType
from .bestaetigung_type import BestaetigungType
from .visnachricht_type import VisnachrichtType
from .zubringernachricht_type import ZubringernachrichtType


@dataclass(kw_only=True)
class DatenAbrufenAntwortType:
    bestaetigung: BestaetigungType = field(
        metadata={
            "name": "Bestaetigung",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    weitere_daten: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WeitereDaten",
            "type": "Element",
            "namespace": "",
        },
    )
    choice: List[
        Union[
            ZubringernachrichtType,
            AbbringernachrichtType,
            AzbnachrichtType,
            VisnachrichtType,
            AndnachrichtType,
            AusnachrichtType,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Zubringernachricht",
                    "type": ZubringernachrichtType,
                    "namespace": "",
                },
                {
                    "name": "Abbringernachricht",
                    "type": AbbringernachrichtType,
                    "namespace": "",
                },
                {
                    "name": "AZBNachricht",
                    "type": AzbnachrichtType,
                    "namespace": "",
                },
                {
                    "name": "VISNachricht",
                    "type": VisnachrichtType,
                    "namespace": "",
                },
                {
                    "name": "ANDNachricht",
                    "type": AndnachrichtType,
                    "namespace": "",
                },
                {
                    "name": "AUSNachricht",
                    "type": AusnachrichtType,
                    "namespace": "",
                },
            ),
        },
    )
