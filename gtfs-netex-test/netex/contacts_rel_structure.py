from dataclasses import dataclass, field

from .contact import Contact
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContactsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "contacts_RelStructure"

    contact: list[Contact] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
