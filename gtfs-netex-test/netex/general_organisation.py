from dataclasses import dataclass
from .general_organisation_version_structure import (
    GeneralOrganisationVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisation(GeneralOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
