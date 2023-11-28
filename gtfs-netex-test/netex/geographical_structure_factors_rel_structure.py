from dataclasses import dataclass, field
from typing import List
from netex.geographical_structure_factor import GeographicalStructureFactor
from netex.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalStructureFactorsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of GEOGRAPHICAL STRUCTURE FACTOR.
    """
    class Meta:
        name = "geographicalStructureFactors_RelStructure"

    geographical_structure_factor_ref_or_geographical_structure_factor: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactor",
                    "type": GeographicalStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
