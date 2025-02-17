from dataclasses import dataclass

from .other_organisation_version_structure import OtherOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OtherOrganisation(OtherOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
