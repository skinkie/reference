from dataclasses import dataclass
from .type_of_organisation_part_ref_structure import (
    TypeOfOrganisationPartRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfOrganisationPartRef(TypeOfOrganisationPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RestrictedVar
