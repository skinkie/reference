from dataclasses import dataclass, field
from netex.contact import Contact
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ContactsRelStructure(ContainmentAggregationStructure):
    """Type for containment in frame of reusable CONTACT details.

    +v1.2.2
    """
    class Meta:
        name = "contacts_RelStructure"

    contact: Contact = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
