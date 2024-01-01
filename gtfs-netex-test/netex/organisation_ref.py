from dataclasses import dataclass
from .organisation_ref_structure import OrganisationRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationRef(OrganisationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
