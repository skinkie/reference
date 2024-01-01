from dataclasses import dataclass
from .other_organisation_ref_structure import OtherOrganisationRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisationRefStructure(OtherOrganisationRefStructure):
    value: RestrictedVar
