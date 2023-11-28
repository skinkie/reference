from dataclasses import dataclass
from netex.additional_driver_option_ref_structure import AdditionalDriverOptionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AdditionalDriverOptionRef(AdditionalDriverOptionRefStructure):
    """Reference to a ADDITIONAL DRIVER OPTION usage parameter.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
