from dataclasses import dataclass, field
from typing import List

from .fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FareClasses:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
