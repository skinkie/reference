from dataclasses import dataclass
from .other_organisation_version_structure import (
    OtherOrganisationVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisationVersionStructure(OtherOrganisationVersionStructure):
    class Meta:
        name = "GeneralOrganisation_VersionStructure"
