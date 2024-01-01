from dataclasses import dataclass
from .check_constraint_version_structure import CheckConstraintVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraint(CheckConstraintVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
