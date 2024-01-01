from dataclasses import dataclass
from .duty_part_version_structure import DutyPartVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DutyPart(DutyPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
