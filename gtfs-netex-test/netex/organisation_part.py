from dataclasses import dataclass

from .organisation_part_version_structure import OrganisationPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OrganisationPart(OrganisationPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
