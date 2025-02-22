from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .sections_in_sequence_rel_structure import CommonSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CommonSectionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "commonSectionsInFrame_RelStructure"

    common_section: list[CommonSection] = field(
        default_factory=list,
        metadata={
            "name": "CommonSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
