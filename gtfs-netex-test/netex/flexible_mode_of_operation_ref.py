from dataclasses import dataclass
from netex.flexible_mode_of_operation_ref_structure import FlexibleModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleModeOfOperationRef(FlexibleModeOfOperationRefStructure):
    """
    Reference to a FLEXIBLE MODE OF OPERATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
