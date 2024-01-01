from dataclasses import dataclass
from .department_version_structure import DepartmentVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Department(DepartmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
