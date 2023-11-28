from dataclasses import dataclass, field
from netex.operating_department_version_structure import OperatingDepartmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDepartment(OperatingDepartmentVersionStructure):
    """
    A specific DEPARTMENT which administers certain LINEs.

    :ivar id: Identifier of  OPERATING DEPARTMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
