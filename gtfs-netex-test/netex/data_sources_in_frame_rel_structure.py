from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.data_source import DataSource

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataSourcesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DATA SOURCE.
    """
    class Meta:
        name = "dataSourcesInFrame_RelStructure"

    data_source: List[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
