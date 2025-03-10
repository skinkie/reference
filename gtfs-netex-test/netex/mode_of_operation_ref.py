from dataclasses import dataclass

from .mode_of_operation_ref_structure import ModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ModeOfOperationRef(ModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
