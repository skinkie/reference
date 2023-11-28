from dataclasses import dataclass
from netex.rental_option_ref_structure import RentalOptionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalOptionRef(RentalOptionRefStructure):
    """Reference to a RENTAL OPTION usage parameter.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
