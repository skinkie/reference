from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDateTime
from .abbringer_info_type import AbbringerInfoType
from .fahrt_filter_type import FahrtFilterType
from .zeit_filter_type import ZeitFilterType


@dataclass(kw_only=True)
class AboAsbtype:
    class Meta:
        name = "AboASBType"

    asbid: str = field(
        metadata={
            "name": "ASBID",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )
    zeit_filter_or_fahrt_filter: List[
        Union[ZeitFilterType, FahrtFilterType]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ZeitFilter",
                    "type": ZeitFilterType,
                    "namespace": "",
                },
                {
                    "name": "FahrtFilter",
                    "type": FahrtFilterType,
                    "namespace": "",
                },
            ),
        },
    )
    hysterese: int = field(
        metadata={
            "name": "Hysterese",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    abbringer_info: Optional[AbbringerInfoType] = field(
        default=None,
        metadata={
            "name": "AbbringerInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    abo_id: int = field(
        metadata={
            "name": "AboID",
            "type": "Attribute",
            "required": True,
        }
    )
    verfall_zst: XmlDateTime = field(
        metadata={
            "name": "VerfallZst",
            "type": "Attribute",
            "required": True,
        }
    )
