from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.contact_details_structure import ContactDetailsStructure
from netex.contact_type_enumeration import ContactTypeEnumeration
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ContactVersionStructure(DataManagedObjectStructure):
    """
    Type for an CONTACT.

    :ivar name: The name of the CONTACT.
    :ivar contact_details: Contact details for CONTACT.
    :ivar contact_type: Classification of ContactTy[e. Used for
        arbitrary documentation.
    """
    class Meta:
        name = "Contact_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contact_details: Optional[ContactDetailsStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contact_type: Optional[ContactTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ContactType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
