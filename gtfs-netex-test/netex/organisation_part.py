from dataclasses import dataclass, field
from netex.organisation_part_version_structure import OrganisationPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationPart(OrganisationPartVersionStructure):
    """
    A named subdivision of an ORGANISATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
