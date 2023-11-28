from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.related_organisation import RelatedOrganisation

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RelatedOrganisationsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of RELATED ORGANISATIONs.
    """
    class Meta:
        name = "relatedOrganisations_RelStructure"

    related_organisation: List[RelatedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "RelatedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
