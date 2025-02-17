from dataclasses import dataclass

from .organisation_part_ref_structure import OrganisationPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OrganisationPartRef(OrganisationPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
