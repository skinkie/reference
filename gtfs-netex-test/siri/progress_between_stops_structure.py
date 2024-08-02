from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProgressBetweenStopsStructure:
    link_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LinkDistance",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
