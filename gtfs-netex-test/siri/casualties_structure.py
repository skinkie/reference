from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CasualtiesStructure:
    number_of_deaths: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfDeaths",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number_of_injured: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfInjured",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
