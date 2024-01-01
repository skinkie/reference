from dataclasses import dataclass
from .organisational_unit_ref_structure import OrganisationalUnitRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnitRef(OrganisationalUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
