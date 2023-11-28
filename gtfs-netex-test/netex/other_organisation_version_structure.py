from dataclasses import dataclass, field
from typing import Optional
from netex.organisation_version_structure import OrganisationVersionStructure
from netex.postal_address_version_structure import PostalAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OtherOrganisationVersionStructure(OrganisationVersionStructure):
    """
    Type for an OTHER ORGANISATION.

    :ivar address: Address of ORGANISATION.
    """
    class Meta:
        name = "OtherOrganisation_VersionStructure"

    address: Optional[PostalAddressVersionStructure] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
