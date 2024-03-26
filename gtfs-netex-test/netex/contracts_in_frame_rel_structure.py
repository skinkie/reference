from dataclasses import dataclass

from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContractsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "contractsInFrame_RelStructure"
