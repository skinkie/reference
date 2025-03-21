from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .data_source import DataSource

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DataSourcesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dataSourcesInFrame_RelStructure"

    data_source: list[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
