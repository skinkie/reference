from dataclasses import dataclass

from .additional_driver_option_ref_structure import AdditionalDriverOptionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdditionalDriverOptionRef(AdditionalDriverOptionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
