from dataclasses import dataclass, field
from typing import Optional
from netex.department_version_structure import DepartmentVersionStructure
from netex.operational_contex_refs_rel_structure import OperationalContexRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDepartmentVersionStructure(DepartmentVersionStructure):
    """
    Type for an OPERATING DEPARTMENT.

    :ivar operational_contexts: OPERATIONAL CONTEXTs for OPERATING
        DEPARTMENT.
    """
    class Meta:
        name = "OperatingDepartment_VersionStructure"

    operational_contexts: Optional[OperationalContexRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "operationalContexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
