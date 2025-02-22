from dataclasses import dataclass

from .rental_option_version_structure import RentalOptionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RentalOption(RentalOptionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
