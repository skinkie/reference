from dataclasses import dataclass

from .type_of_organisation_part_ref_structure import TypeOfOrganisationPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfOrganisationPartRef(TypeOfOrganisationPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
