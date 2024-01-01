from dataclasses import dataclass
from .value_set_version_structure import ValueSetVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValueSet(ValueSetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
