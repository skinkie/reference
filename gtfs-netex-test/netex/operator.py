from dataclasses import dataclass
from .operator_version_structure import OperatorVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Operator(OperatorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
