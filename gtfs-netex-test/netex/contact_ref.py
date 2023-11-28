from dataclasses import dataclass
from netex.contact_ref_structure import ContactRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ContactRef(ContactRefStructure):
    """Reference to a CONTACT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
