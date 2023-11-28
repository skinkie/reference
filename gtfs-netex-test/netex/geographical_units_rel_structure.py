from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.geographical_unit import GeographicalUnit
from netex.geographical_unit_ref import GeographicalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnitsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of GEOGRAPHICAL UNITs.
    """
    class Meta:
        name = "geographicalUnits_RelStructure"

    geographical_unit_ref_or_geographical_unit: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalUnitRef",
                    "type": GeographicalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnit",
                    "type": GeographicalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
