from dataclasses import dataclass, field
from typing import Optional
from netex.transport_organisation_version_structure import TransportOrganisationVersionStructure
from netex.type_of_organisation_refs_rel_structure import TypeOfOrganisationRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AuthorityVersionStructure(TransportOrganisationVersionStructure):
    """
    Type for an AUTHORITY.

    :ivar authority_types: Classification of Zone. Used for arbitrary
        documentation -.
    """
    class Meta:
        name = "Authority_VersionStructure"

    authority_types: Optional[TypeOfOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "authorityTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
