from dataclasses import dataclass

from .rental_option_ref_structure import RentalOptionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdditionalDriverOptionRefStructure(RentalOptionRefStructure):
    pass
