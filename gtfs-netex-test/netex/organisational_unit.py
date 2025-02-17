from dataclasses import dataclass

from .organisational_unit_version_structure import OrganisationalUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OrganisationalUnit(OrganisationalUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
