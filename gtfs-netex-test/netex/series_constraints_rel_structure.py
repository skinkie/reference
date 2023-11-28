from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.series_constraint import SeriesConstraint
from netex.series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SERIES ELEMENTs.
    """
    class Meta:
        name = "SeriesConstraints_RelStructure"

    series_constraint_ref_or_series_constraint: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SeriesConstraintRef",
                    "type": SeriesConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraint",
                    "type": SeriesConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
