from dataclasses import dataclass

from .contact_ref_structure import ContactRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ContactRef(ContactRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
