from dataclasses import dataclass
from netex.transferability_ref_structure import TransferabilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferabilityRef(TransferabilityRefStructure):
    """
    Reference to a TRANSFERABILITY USAGE PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
