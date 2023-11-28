from dataclasses import dataclass
from netex.department_ref_structure import DepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDepartmentRefStructure(DepartmentRefStructure):
    """
    Type for a reference to an OPERATING DEPARTMENT.
    """
