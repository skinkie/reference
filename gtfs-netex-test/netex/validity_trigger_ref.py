from dataclasses import dataclass
from .validity_trigger_ref_structure import ValidityTriggerRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityTriggerRef(ValidityTriggerRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
