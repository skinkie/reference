from dataclasses import dataclass, field
from typing import Optional
from netex.department_ref import DepartmentRef
from netex.organisation_part_version_structure import OrganisationPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationalUnitVersionStructure(OrganisationPartVersionStructure):
    """
    Type for a ORGANISATIONAL UNIT.
    """
    class Meta:
        name = "OrganisationalUnit_VersionStructure"

    department_ref: Optional[DepartmentRef] = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
