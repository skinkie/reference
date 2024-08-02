from dataclasses import dataclass

from .operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ArrivalOperatorRefs(OperatorRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
