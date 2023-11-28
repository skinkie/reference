from dataclasses import dataclass
from netex.rental_option_ref_structure import RentalOptionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AdditionalDriverOptionRefStructure(RentalOptionRefStructure):
    """
    Type for Reference to a ADDITIONAL DRIVER OPTION usage parameter.
    """
