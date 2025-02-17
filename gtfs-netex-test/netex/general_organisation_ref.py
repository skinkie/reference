from dataclasses import dataclass

from .general_organisation_ref_structure import GeneralOrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeneralOrganisationRef(GeneralOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
