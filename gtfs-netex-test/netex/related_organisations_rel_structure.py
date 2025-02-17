from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .related_organisation import RelatedOrganisation

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RelatedOrganisationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "relatedOrganisations_RelStructure"

    related_organisation: list[RelatedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "RelatedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
