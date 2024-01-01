from dataclasses import dataclass
from .contact_ref_structure import ContactRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContactRef(ContactRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
