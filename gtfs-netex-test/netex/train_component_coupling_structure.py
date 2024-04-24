from dataclasses import dataclass, field
from typing import Optional

from .through_access_enumeration import ThroughAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentCouplingStructure:
    splittable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Splittable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    through_access: ThroughAccessEnumeration = field(
        metadata={
            "name": "ThroughAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
