from dataclasses import dataclass
from .type_of_organisation_ref_structure import TypeOfOrganisationRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfOrganisationRef(TypeOfOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
