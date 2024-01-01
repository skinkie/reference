from dataclasses import dataclass
from .general_organisation_ref_structure import GeneralOrganisationRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisationRef(GeneralOrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
