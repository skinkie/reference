from dataclasses import dataclass, field
from netex.related_organisation_version_structure import RelatedOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RelatedOrganisation(RelatedOrganisationVersionStructure):
    """A formal relationship with another  ORGANISATION.

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
