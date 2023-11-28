from dataclasses import dataclass, field
from netex.contact_version_structure import ContactVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Contact(ContactVersionStructure):
    """Reusable CONTACT details for an ORGANISATION or other entity.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
