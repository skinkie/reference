from dataclasses import dataclass
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponsibilityRolesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of RESPONSIBILITY ROLEs.
    """
    class Meta:
        name = "responsibilityRolesInFrame_RelStructure"
