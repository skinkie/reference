from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ReviewStructure:
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ranking: int = field(
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 5,
        }
    )
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_acronym: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "UserAcronym",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
