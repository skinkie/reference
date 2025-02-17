from dataclasses import dataclass

from .operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OperatorRef(OperatorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
