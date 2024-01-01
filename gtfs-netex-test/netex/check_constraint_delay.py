from dataclasses import dataclass
from .check_constraint_delay_version_structure import (
    CheckConstraintDelayVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintDelay(CheckConstraintDelayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
