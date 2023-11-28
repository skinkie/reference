from dataclasses import dataclass, field
from typing import Optional
from netex.contact_details_structure import ContactDetailsStructure
from netex.contact_ref import ContactRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ContactStructure(ContactDetailsStructure):
    """
    Contact details with reference to CONTACT.
    """
    contact_ref: Optional[ContactRef] = field(
        default=None,
        metadata={
            "name": "ContactRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
