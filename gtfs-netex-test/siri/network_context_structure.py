from dataclasses import dataclass, field
from typing import List, Optional

from .affected_operator_structure import AffectedOperatorStructure
from .network_structure import NetworkStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NetworkContextStructure:
    operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network: Optional[NetworkStructure] = field(
        default=None,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
