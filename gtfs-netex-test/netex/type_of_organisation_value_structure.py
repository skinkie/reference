from dataclasses import dataclass

from .type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfOrganisationValueStructure(TypeOfEntityVersionStructure):
    class Meta:
        name = "TypeOfOrganisation_ValueStructure"
