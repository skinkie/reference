from dataclasses import dataclass, field
from typing import Optional, Union

from .encumbrance_enumeration import EncumbranceEnumeration
from .medical_need_enumeration import MedicalNeedEnumeration
from .mobility_enumeration import MobilityEnumeration
from .pyschosensory_need_enumeration import PyschosensoryNeedEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class UserNeedStructure:
    mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need: Optional[Union[MobilityEnumeration, PyschosensoryNeedEnumeration, MedicalNeedEnumeration, EncumbranceEnumeration]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityNeed",
                    "type": MobilityEnumeration,
                    "namespace": "http://www.ifopt.org.uk/acsb",
                },
                {
                    "name": "PsychosensoryNeed",
                    "type": PyschosensoryNeedEnumeration,
                    "namespace": "http://www.ifopt.org.uk/acsb",
                },
                {
                    "name": "MedicalNeed",
                    "type": MedicalNeedEnumeration,
                    "namespace": "http://www.ifopt.org.uk/acsb",
                },
                {
                    "name": "EncumbranceNeed",
                    "type": EncumbranceEnumeration,
                    "namespace": "http://www.ifopt.org.uk/acsb",
                },
            ),
        },
    )
    excluded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    need_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "NeedRanking",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    extensions: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
