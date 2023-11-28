from dataclasses import dataclass
from netex.operating_department_ref_structure import OperatingDepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDepartmentRef(OperatingDepartmentRefStructure):
    """
    Reference to an OPERATING DEPARTMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
