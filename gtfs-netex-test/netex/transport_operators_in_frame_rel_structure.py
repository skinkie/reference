from dataclasses import dataclass, field
from typing import List
from netex.authority import Authority
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.operator import Operator

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportOperatorsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TRANSPORT OPERATORs.
    """
    class Meta:
        name = "transportOperatorsInFrame_RelStructure"

    authority_or_operator: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
