from dataclasses import dataclass, field
from typing import List

from .access_facility import AccessFacility

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MobilityDisruptionStructure:
    mobility_impaired_access: bool = field(
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    access_facility: List[AccessFacility] = field(
        default_factory=list,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
