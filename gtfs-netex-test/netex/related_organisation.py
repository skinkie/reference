from dataclasses import dataclass
from .related_organisation_version_structure import (
    RelatedOrganisationVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RelatedOrganisation(RelatedOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
